# bazel-example

## System Requirements

- [bazelisk](https://bazel.build/install/bazelisk)

## Commands

build: `bazel build ...`

test: `bazel test ...`

### python

add dep:
Mention it in `python_deps/requirements.txt`

generate lock:
`pip freeze`

run:
`bazel run //projects/calculator`

### nodejs

npm install:
`bazel run @yarn//:yarn`

add dep and update lock:
`bazel run @yarn//:yarn -- add <package>`

run:
`bazel run //projects/calc_web`