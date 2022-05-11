# read-spack-db

This repo is a really simple example of downloading a Spack build cache index, reading
it in, and printing the results of a query.

To use:

```
. $spack_prefix/share/spack/setup-env.sh
make run
```

This will download (`make download`) the `index.json` from
`https://cache.e4s.io/build_cache/index.json`, read it, and print out all the versions
of `adiak` in the index.
