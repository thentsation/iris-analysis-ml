# CHANGELOG

<!-- version list -->

## v1.0.4 (2026-10-26)

### Bug Fixes

- **deps**: Upgrade lockfile and use --upgrade in lockfile workflow
  ([#28](https://github.com/thentsation/iris-analysis-ml/pull/28),
  [`5e1b551`](https://github.com/thentsation/iris-analysis-ml/commit/5e1b551ad26e05f51464d939a5e953a1c5aa0922))

- **deps**: Use --upgrade when regenerating the lockfile
  ([#28](https://github.com/thentsation/iris-analysis-ml/pull/28),
  [`5e1b551`](https://github.com/thentsation/iris-analysis-ml/commit/5e1b551ad26e05f51464d939a5e953a1c5aa0922))

### Chores

- **ci**: Bump astral-sh/setup-uv from 10.2.0 to 10.3.0
  ([#20](https://github.com/thentsation/iris-analysis-ml/pull/20),
  [`11dfe82`](https://github.com/thentsation/iris-analysis-ml/commit/11dfe82cd47c199381d3800371b3d56fe1f853bf))

- **ci**: Bump astral-sh/setup-uv from 10.3.0 to 10.3.2
  ([#24](https://github.com/thentsation/iris-analysis-ml/pull/24),
  [`cd12206`](https://github.com/thentsation/iris-analysis-ml/commit/cd122062356fdf85d3d0f88d71dc46ccb2409cb8))

- **deps**: Bump nbconvert from 7.17.1 to 7.17.2 in /config
  ([#22](https://github.com/thentsation/iris-analysis-ml/pull/22),
  [`3dd3c39`](https://github.com/thentsation/iris-analysis-ml/commit/3dd3c39c99cf7a3b8dca9f7a36ee709eaf9c0aba))

- **deps**: Bump python from 3.12-slim to 3.14-slim in /docker
  ([#12](https://github.com/thentsation/iris-analysis-ml/pull/12),
  [`0488c0a`](https://github.com/thentsation/iris-analysis-ml/commit/0488c0a687b31d88eae598ccb627a35ef48fbd27))

- **deps**: Bump ruff from 0.16.10 to 0.17.0 in /config
  ([#21](https://github.com/thentsation/iris-analysis-ml/pull/21),
  [`2bd0223`](https://github.com/thentsation/iris-analysis-ml/commit/2bd02238cd8e3489fb4c2e46f2662c7001e4c36f))

- **deps**: Bump ruff from 0.17.0 to 0.17.1 in /config
  ([#23](https://github.com/thentsation/iris-analysis-ml/pull/23),
  [`eb3dd50`](https://github.com/thentsation/iris-analysis-ml/commit/eb3dd50078bf4a892bcf1de73d3a339684a9a13b))

- **deps**: Refresh pip-compile outputs
  ([#17](https://github.com/thentsation/iris-analysis-ml/pull/17),
  [`b56d59b`](https://github.com/thentsation/iris-analysis-ml/commit/b56d59bff6e5eeaf3c20a48eb0c4d9ca0a43688d))

- **deps**: Update dependency mypy to v2.4.0
  ([#15](https://github.com/thentsation/iris-analysis-ml/pull/15),
  [`e2279e5`](https://github.com/thentsation/iris-analysis-ml/commit/e2279e53e2d6b78aab98d9ce1f8885fbec901e03))

- **deps**: Update dependency ruff to v0.16.10
  ([#14](https://github.com/thentsation/iris-analysis-ml/pull/14),
  [`6ab8398`](https://github.com/thentsation/iris-analysis-ml/commit/6ab8398eb7d57198dafee9fa4e38faf893a2dddf))

- **deps**: Update lockfile ([#28](https://github.com/thentsation/iris-analysis-ml/pull/28),
  [`5e1b551`](https://github.com/thentsation/iris-analysis-ml/commit/5e1b551ad26e05f51464d939a5e953a1c5aa0922))

- **deps**: Update pandas requirement in /config
  ([#26](https://github.com/thentsation/iris-analysis-ml/pull/26),
  [`a64ed06`](https://github.com/thentsation/iris-analysis-ml/commit/a64ed06102b76e025bf491829eef52c922282767))

### Continuous Integration

- Pipeline da Shared Library da plataforma e Renovate
  ([#13](https://github.com/thentsation/iris-analysis-ml/pull/13),
  [`9b77dce`](https://github.com/thentsation/iris-analysis-ml/commit/9b77dcefab34141c160bd962687f12c990ab5006))

- Remove workflow notify-portfolio (token sem acesso; o portfolio atualiza pelo cron diário)
  ([#19](https://github.com/thentsation/iris-analysis-ml/pull/19),
  [`fbfa4ec`](https://github.com/thentsation/iris-analysis-ml/commit/fbfa4eceb5dccec36c03bea34194566da9ce6445))


## v1.0.3 (2026-09-28)

### Bug Fixes

- **ci**: Open lockfile PRs with RELEASE_PAT so CI runs on them
  ([`fcd7840`](https://github.com/thentsation/iris-analysis-ml/commit/fcd784018bd757d4a19d4af7b88110f631321895))

### Chores

- **deps**: Ignore numpy 2.5+ in dependabot
  ([`0772741`](https://github.com/thentsation/iris-analysis-ml/commit/07727419df008cbff9318c146e9d8f86bd12dc14))

- **deps**: Update matplotlib requirement in /config
  ([#3](https://github.com/thentsation/iris-analysis-ml/pull/3),
  [`8ad4747`](https://github.com/thentsation/iris-analysis-ml/commit/8ad4747793e1d26d90a22948f8532b259cc47229))

- **deps**: Update numpy requirement in /config
  ([#10](https://github.com/thentsation/iris-analysis-ml/pull/10),
  [`f21c1a1`](https://github.com/thentsation/iris-analysis-ml/commit/f21c1a1498dbb47e2da69b748fc156020031a94e))

- **deps**: Update pandas requirement in /config
  ([#9](https://github.com/thentsation/iris-analysis-ml/pull/9),
  [`e63e58f`](https://github.com/thentsation/iris-analysis-ml/commit/e63e58f6a1ffc8774abe665eead5f15b53293bef))

- **deps**: Update scikit-learn requirement in /config
  ([#8](https://github.com/thentsation/iris-analysis-ml/pull/8),
  [`f65c994`](https://github.com/thentsation/iris-analysis-ml/commit/f65c9948d6cde37ed8209c0fda3ecb02cef39387))

- **deps**: Update seaborn requirement in /config
  ([#5](https://github.com/thentsation/iris-analysis-ml/pull/5),
  [`13d3dfc`](https://github.com/thentsation/iris-analysis-ml/commit/13d3dfcab3e2615de5b0dd82836d4c9279e053b4))


## v1.0.2 (2026-09-28)

### Bug Fixes

- Use RELEASE_PAT so dependabot auto-merge can write to PRs
  ([`0268263`](https://github.com/thentsation/iris-analysis-ml/commit/0268263ec787fd20ffa2f2d293ed153ec7602c99))

### Chores

- **deps**: Bump ruff from 0.16.3 to 0.16.9 in /config
  ([#7](https://github.com/thentsation/iris-analysis-ml/pull/7),
  [`e12c952`](https://github.com/thentsation/iris-analysis-ml/commit/e12c9527e1bfcc1a722d1f36c6ecbbcef73d15d3))


## v1.0.1 (2026-09-26)

### Bug Fixes

- Broaden Trivy's pip/_vendor skip-dirs to a recursive glob
  ([`16ff464`](https://github.com/thentsation/iris-analysis-ml/commit/16ff464cf0738faf756aa8957a52595fed901edb))

### Chores

- **deps**: Bump nbconvert from 7.16.6 to 7.17.1 in /config
  ([#4](https://github.com/thentsation/iris-analysis-ml/pull/4),
  [`303d876`](https://github.com/thentsation/iris-analysis-ml/commit/303d8766d4d37f51dca22a4074264f7868161afe))
