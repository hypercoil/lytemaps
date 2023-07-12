# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
Noxfile
"""
import nox

@nox.session()
def clean(session):
    session.install('coverage[toml]')
    session.run('coverage', 'erase')

@nox.session(python=['3.8', '3.9', '3.10', '3.11'])
def tests(session):
    session.install('.')
    session.install('coverage[toml]')
    session.install('pytest')
    session.install('pytest-cov')
    session.install('ruff')
    session.run(
        'pytest',
        '--cov', 'lytemaps',
        '--cov-append',
        'tests/',
    )
    session.run('ruff', 'check', 'src/lytemaps')

@nox.session()
def report(session):
    session.install('coverage[toml]')
    session.run(
        'coverage',
        'report',
        "--omit='*test*,*__init__*'",
    )
    session.run(
        'coverage',
        'html',
        "--omit='*test*,*__init__*'",
    )
    session.run(
        'coverage',
        'xml',
        "--omit='*test*,*__init__*'",
    )
