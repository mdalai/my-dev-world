
# Ansible Dev Tips

- Ansible is idempotent. If Apache is already install, it won't install it.
- Set `host_key_checking = false` in ansible.cfg if ansible throws connection failure. 
- Conditional execution via WHEN statement.
- Ignore errors and fail at end. Use `ignore_errors: true` for each task. Use `register: result`. At the end of playbook, add a task:

```yaml
-name: Set flag
 set_fact: flag = failed
 failed_when: result is failed
```

```sh

# Run ansible playbook start from certain task
ansible-playbook tasks.yml --start-at-task "TaskName"

# Run through tasks interactively
ansible-playbook tasks.yml --step

# Run with check mode
ansible-playbook tasks.yml --start-at-task "TaskName" --check
```