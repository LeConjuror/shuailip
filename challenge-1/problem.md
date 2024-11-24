# Echo Valley

- Namespace: picoctf/18739f24
- ID: echo-valley
- Type: custom
- Category: Binary Exploitation
- Points: 1
- Templatable: no
- MaxUsers: 1

## Description

The echo valley is a simple function that echoes back 
whatever you say to it.

But how do you make it responds with sth more interesting, like a flag?

## Details

Connect to the service at `nc {{server}} {{port}}`
Download the program: {{url_for("valley.c")}}


## Hints

- Ever heard of format string attack?

## Solution Overview

Check `solution.py` comments for a detailed walkthrough.

TLDR:
1. Use %p to bypass PIE and print out the stack to find out 
about where the stack and code are.
2. Use %n to bypass the canary and overwrite the return address 
of echo_valley() with the address of print_flag().
3. Returns from echo_valley() and profit.

## Challenge Options

## Learning Objective

Format String goes brrrrrr

## Attributes

- author: Shuailin Pan (LeConjuror)
