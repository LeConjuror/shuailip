# RED

- Namespace: picoctf/18739f24
- ID: redredredred
- Type: custom
- Category: Reverse Engineering
- Points: 40
- Templatable: no
- MaxUsers: 1

## Description

RED, RED, RED, RED

## Details

Download the image: {{url_for("red.png")}}

## Hints

- The picture seems pure, but is it though?
- Red?Ged?Bed?Aed?
- Check whatever facebook is called now.

## Solution Overview

Check `solution.py` comments for a detailed walkthrough.

The picture uses classic steganography technique where the
least significant bit of each of the rgba channel is used to
hide data (two pixels -> 8bits -> 1 char).

In this specific problem, each row of pixel (128) hides the
same binary ascii representation of the base64 encoded string
of the solution flag.

## Challenge Options

## Learning Objective

Pattern recognition, scripting skills

## Attributes

- author: Shuailin Pan (LeConjuror)
