# easycmd

A command line tool which stores annoying command and its nickname

### Install

```
bash install.sh
```

### Usage

1. Store an annoying command

```bash
easycmd cache annoying-complex-fking-command
# Or with an alias
# easycmd cache annoying-complex-fking-command -a test

# If you want to store commands with parameters
# easycmd cache "another command -with parameter"
```

2. Search the annoying command by entering part of it or its alias

```
easycmd find anno
```

The output shall be

```
ALIAS: annoying-complex-fking-command CMD: annoying-complex-fking-command
```