# Tiny Chess Engine — make.fun tiny-chess-01

Engine catur Python ≤4.096 byte untuk bounty make.fun
"Build the strongest chess engine in 4 KB of Python".

## Cara main

`main.py` adalah satu file mandiri (Python 3.13, stdlib saja). Ia membaca
`MAKEFUN_ENV_URL`, memainkan 8 game gauntlet lewat HTTP (`/game`, `/move`),
dan mengirim langkah dalam format UCI. Tidak ada panggilan model, tidak ada
jam: pencarian memakai budget node tetap (deterministik).

## Isi engine

- Papan 120-kotak, move generator pseudo-legal + filter legalitas (termasuk
  rokade, en passant, promosi).
- Alpha-beta + quiescence search (tangkapan + promosi), iterative deepening
  dengan budget node tetap.
- Evaluasi material + piece-square tables (Michniewski).
- Transposition table (Zobrist), move ordering MVV-LVA + TT move.
- Budget node default 100.000/langkah (env `NODE_BUDGET`).

`main.py` adalah payload lzma + unpacker (diizinkan aturan); source
lengkapnya dikembangkan di `chess-dev/` dan diminify sebelum dipack.

## Lisensi

MIT — lihat LICENSE.
