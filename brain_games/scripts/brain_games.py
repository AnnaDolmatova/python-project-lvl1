#!/usr/bin/env python
import prompt


def welcome_user(name):
    print('Hello, {}!'.format(name))


def hello(who):
    print("Welcome to the {}!".format(who))


def main():
    hello('Brain Games')
    name = prompt.string('May I have your name? ')
    welcome_user(name)


if __name__ == "__main__":
    main()
