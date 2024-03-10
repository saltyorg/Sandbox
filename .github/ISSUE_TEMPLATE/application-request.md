---
name: Application request
about: Suggest an app for this project
description: Suggest an app for this project
title: '[Req]: '
labels: ''
assignees: ''

---

body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to request an application!
  - type: input
    id: contact
    attributes:
      label: Contact Details
      description: How can we get in touch with you if we need more info?
      placeholder: ex. email@example.com
    validations:
      required: false
  - type: textarea
    id: what-is-it
    attributes:
      label: What is it?
      description: What is the name of the application and what does it do?
      placeholder: FooApp is useful for Binging Bangs to prepare them for Boing.
      value: "Gimme Shock Treatment!"
    validations:
      required: true

  - type: textarea
    id: why-is-it
    attributes:
      label: Why does this belong in Sandbox?
      description: What makes the application a good fit for Sandbox?
      placeholder: Many people required well-binged bangs.
      value: "Suzy is a Punk Rocker!"
    validations:
      required: true
  - type: textarea
    id: docker
    attributes:
      label: Link to docker
      description: Please provide a link to the desired docker image.
      render: shell
    validations:
      required: true
  - type: textarea
    id: docker
    attributes:
      label: Link to docs
      description: Please provide a link to any available setup documentation.
      render: shell
