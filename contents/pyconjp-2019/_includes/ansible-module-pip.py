def main():
    state_map = dict(
        present=['install'],
        absent=['uninstall', '-y'],
        latest=['install', '-U'],
        forcereinstall=['install', '-U', '--force-reinstall'],
    )

    module = AnsibleModule(
        # モジュールの設定定義：省略
    )

    try:
        # pipコマンドのの定義
        pip = _get_pip(module, env, module.params['executable'])
        # 求める状態に応じて、どのサブコマンドが必要かを決定
        cmd = [pip] + state_map[state]

        # pipコマンドを作っていく過程
        if extra_args:
            cmd.extend(shlex.split(extra_args))

        if name:
            cmd.extend(to_native(p) for p in packages)
        elif requirements:
            cmd.extend(['-r', requirements])
        else:
            module.exit_json(
                changed=False,
                warnings=["No valid name or requirements file found."],
            )

        rc, out_pip, err_pip = module.run_command(cmd, path_prefix=path_prefix, cwd=chdir)
        out += out_pip
        err += err_pip
        if rc == 1 and state == 'absent' and \
           ('not installed' in out_pip or 'not installed' in err_pip):
            pass  # rc is 1 when attempting to uninstall non-installed package
        elif rc != 0:
            _fail(module, cmd, out, err)

        if state == 'absent':
            changed = 'Successfully uninstalled' in out_pip
        else:
            if out_freeze_before is None:
                changed = 'Successfully installed' in out_pip
            else:
                _, out_freeze_after, _ = _get_packages(module, pip, chdir)
                changed = out_freeze_before != out_freeze_after

        changed = changed or venv_created

        module.exit_json(changed=changed, cmd=cmd, name=name, version=version,
                         state=state, requirements=requirements, virtualenv=env,
                         stdout=out, stderr=err)
    finally:
        if old_umask is not None:
            os.umask(old_umask)
