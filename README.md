# OpenConsole

> We have to go where they can’t follow.

OpenConsole is an x64 UEFI-first game launcher intended to live on a USB drive
beside signed, portable OCG games. Select the drive as a firmware boot target and
the machine opens directly into your library—no installed operating system and
no proprietary storefront runtime.

The aim is ambitious: one day, carry quality games between virtually any
computer. The present release is narrower: a **disposable-OVMF development
preview** with a software graphics reference path. Broad physical hardware,
Secure Boot enrollment, complete GLES 2 conformance, and AMD acceleration are
not claimed.

## Start here

- [Developer documentation](https://openconsole-araujota97gmailcoms-projects.vercel.app/docs)
- [Build your first game](https://openconsole-araujota97gmailcoms-projects.vercel.app/docs/v0.1/quickstart)
- [Browse signed games](https://openconsole-araujota97gmailcoms-projects.vercel.app)
- [Catalog source](https://github.com/araujota/openconsole-catalog)
- [Project status](docs/status.md) and [threat model](docs/threat-model.md)

```sh
make test-host check-examples check-efi-core
python3 scripts/build-development-image.py
python3 scripts/build-release-candidate.py
./scripts/verify-release-clean.sh
```

Game authors use ordinary freestanding C, Zig, or Rust, a small versioned ABI,
manifest v2, raw OCJ1 jacket pixels, and deterministic Ed448-signed OCG2
bundles. EFI children are trusted native firmware code; signatures and static
analysis are not a sandbox.

Apache-2.0. Read [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md),
and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before participating.
