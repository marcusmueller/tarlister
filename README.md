# tarlister

This is just a quick tool to read the first few entries from an archive (or
tape), as long the archive type is supported by
[libarchive](https://www.libarchive.org). And there's
[many](https://github.com/libarchive/libarchive/wiki/LibarchiveFormats); if
your archive is supported by `bsdtar`, it is almost surely supported by this
tool. 

Just run it with `-n 10` to give you the first 10 file names contained in an archive:

```shell
tarlister -n 10 /dev/foo.tar.xz
```

## But why?

[That's why.](https://unix.stackexchange.com/a/801135/106650)
