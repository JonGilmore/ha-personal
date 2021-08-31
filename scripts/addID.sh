#!/bin/bash

for file in $(ls new-*.yaml); do
  mv "$file" "${file/new\-/}"
done