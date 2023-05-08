from flask import Flask
from flask import render_template, request, redirect, url_for, flash, Blueprint
from website import create_app
from flask import send_from_directory
import os
import glob
import sys
import binascii
import argparse

app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



