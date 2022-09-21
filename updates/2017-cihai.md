---
orphan: true
---

(cihai-2017)=

# Introducing cihai

## Background

### The subject

- Internationalization and Localization
- Chinese, Japanese, Korean, and Vietnamese Han Characters (CJK)
- Accessibility, interoperability, and tooling

### What is cihai?

Organization that creates tools to normalize and make available CJK data in

### The goal

cihai exists solely to benefit, augment, and supplement what data is already available for the
public good.

## Where cihai exists

Where does cihai exist similar to other projects? The current solutions available in some instances
overlap, so how does cihai stand to help them rather than duplicate effort?

### UNIHAN

cihai leverages Unicode's Han Unification database as a source of truth.

This is by far the most authoritative source of CJK information and standardization.

cihai stands to make UNIHAN's data export more accessible and offer the public ways to export it.

It cannot be understated the amount of public effort goes into making their work possible. Any
persons experimenting or working with HAN Unification are also welcome to leverage cihai in any form
to benefit the primary HAN data set. The intention of cihai's tools is to make it easier.

### CEDict

CEDict is a creative commons licensed dictionary of chinese definitions in the english language.

## Sustainability

cihai tools have been split and engineered to be orthogonal and reuseable as possible.

### Break down of tools

cihai > unihan-db > unihan-etl

Every step along the way, from data normalization, to loading into relational data models, to
front-ends against an ever expanding list of CJK data, the tools are open source. This assures all
time spent on cihai tools have the maximum amount of utility to the public.

#### unihan-etl

allows custom, normalized exports of UNIHAN's databases

A researcher, software developer, or other stakeholder may only seek to retrieve a custom data
export of the UNIHAN database. Such as this [UNICODE mailing list post][unicode mailing list post],
and another comment how many resort to crafting [their own regular
expressions][their own regular expressions] to pull out data.

[unicode mailing list post]: http://unicode.org/mail-arch/unicode-ml/y2004-m04/0255.html
[their own regular expressions]: http://www.unicode.org/mail-arch/unicode-ml/y2017-m05/0186.html

#### unihan-db

unihan-db further allows RDBMS access of the UNIHAN database, based off unihan-etl

#### cihai

cihai uses unihan-db to provide an initial set of data and a spine for further data sets

## Standardization

Key standards embraced in projects by the cihai organization.

### Zero configuration

By default, all tools and libraries should fall back on _portable_ defaults.

Portable - Working across regions and systems

#### Unicode defaults

This assures usage and output of applications work regardless of system's regional settings. This is
especially important as regions where CJK is prominent use [many encoding
types][many encoding types] (hence the creation of {ref}`Han Unification <unihan-etl:unihan>`

[many encoding types]: https://en.wikipedia.org/wiki/Chinese_character_encoding

#### XDG Specification

SQLite

### Easy configuration

- SQLAlchemy engine URL
- XDG template variables
- Environmental template variables

### Documentation

clear explanation of data normalization task and how it's solved

API and usage

### Data normalization

Where possible, cihai offers data sets via the Open Knowledge Foundation's FrictionlessData
standard.

### Permissive licensing

Licensing should be brief and clear and make the software/data as open as possible.

### Stewardship

As an added way to make the tools more sustainable and transparent, the software is licensed to the
cihai organization. Cihai works for the public benefit.
