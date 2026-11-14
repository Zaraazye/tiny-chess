# Tiny Chess Engine — make.fun tiny-chess-01

Engine catur Python ≤4.096 byte untuk bounty make.fun
"Build the strongest chess engine in 4 KB of Python".
Ditulis langsung sebagai kode Python yang bisa dibaca (bukan blob).

## Cara main

`main.py` satu file mandiri (Python 3.13, stdlib saja). Membaca
`MAKEFUN_ENV_URL`, memainkan 8 game gauntlet lewat HTTP (`/game`, `/move`),
dan mengirim langkah dalam format UCI. Tanpa panggilan model, tanpa jam:
pencarian memakai budget node tetap (deterministik).

## Isi engine

- Papan 120-kotak, move generator legal (rokade, en passant, promosi).
- Alpha-beta + quiescence (tangkapan saja), iterative deepening
  dengan budget node tetap.
- Evaluasi material + piece-square table (6 tabel per bidak,
  32 entri, dikodekan ringkas dalam satu string).
- Transposition table sederhana (dict, kunci = papan + giliran).
- Move ordering MVV-LVA + promosi.
- Budget node default 50.000/langkah (env `NODE_BUDGET`).
- `main.py` 4.090 byte (batas 4.096).

## Uji

Perft terverifikasi: start 8.902 (d3), kiwipete 97.862 (d3),
en-passant 2.812 (d3). Trial practice trial-0 (14 Nov 2026):
ELO 1.173 (1 menang, 3 seri, 4 kalah) — di atas floor 1.154.
`./run_trial.sh <trial-dir> 50000 <workdir> <port> main.py`.

## Lisensi

MIT — lihat LICENSE.
