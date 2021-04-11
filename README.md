# Creating Environment Variables

There are 3 ways we will talk about creating and working with environment variables:

*note: shell and terminal are used interchably*

- [Creating Environment Variables](#creating-environment-variables)
  - [Through your shell](#through-your-shell)
  - [With a shell configuration file](#with-a-shell-configuration-file)
  - [With a `.env` file](#with-a-env-file)
    - [Python](#python)
    - [Nodejs](#nodejs)

## Through your shell

You can create an environment variable by running:

```bash
export DOG=PUG
```

And then check to see if you've done it right with:

```bash
echo $DOG
```
And you should see the shell print out `PUG`.

Creating environment variables this way mean that when you close your terminal/shell, you will lose all environment variables.

## With a shell configuration file

If you use environment variables a lot, a better way might be to put them in a [shell configuration file](https://www.computerworld.com/article/2786076/shell-configuration-files.html). 

For example, if you use Bash, you might have a file like `~/.bash_profile` that has the following in it:

```bash
export DOG=PUG
```

This will mean, that every time your user starts up a shell, that environment variable will be set. 

For a shell like `zsh` or `z shell` you can do the same in the `~/.zshenv` file

## With a `.env` file

Sometimes, you want to separate environment variables project to project, so at the home directory of your project, you put all your environment variables in a `.env` file. You'll then have to load those `.env` files into your files specifically. We have a python and nodejs example in this repo.

If your shell already has environment variables, the environment variables in the `.env` will *not* override the ones in your shell. 

### Python

```
from dotenv import load_dotenv
load_dotenv()
```

### Nodejs

```
require('dotenv').config()
```
