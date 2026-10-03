---
⬆️ [[Ana Səhifə]]

# EKOB NEWS PWA — Frontend Komponentləri

**Texnologiya:** React + Next.js + Tailwind CSS (Emergent.sh)
**Tema:** Yaşıl (#10b981) + Gümüşü (slate)

## Fayl Strukturu

```
src/
├── components/
│   ├── Header.jsx        — Logo, axtarış, sosial linklər
│   ├── TickerBar.jsx     — Canlı kripto/səhm qiymətləri (scrolling)
│   ├── CategoryNav.jsx   — 8 kateqoriya naviqasiyası (sticky)
│   ├── NewsCard.jsx      — Xəbər kartı (şəkilli/şəkilsiz, kateqoriya rəngi)
│   ├── NewsGrid.jsx      — Kartlar grid-i + filter + axtarış
│   ├── Footer.jsx        — Alt bilgi, linklər, copyright
├── pages/
│   └── index.jsx         — Ana səhifə (hero, grid, PWA banner)
├── globals.css           — Tailwind konfiq, scrollbar, animasiyalar
public/
└── manifest.json         — PWA manifest
```

## Komponent Detalları

### Header
- Sticky, scroll-da blurlanır
- Logo: gradient emerald `E` hərfi
- Axtarış inputu (canlı filter)
- Sosial media linkləri (FB, IG, TT, TG)

### TickerBar
- Yaşıl-qara gradient fon
- "CANLI" etiketi + pulsing nöqtə
- Sonsuz scrolling animasiya (30s)
- Hər 5 saniyədə qiymət yenilənir (mock → `/api/market-prices`)
- Yaşıl ▲ / qırmızı ▼ dəyişim

### CategoryNav
- 8 kateqoriya: emoji + etiket (mobil: qısa)
- Aktiv kateqoriya emerald-600 arxa fon
- Sticky (z-40)
- Üfüqi scroll (overflow-x-auto)

### NewsCard
- Sol kənar rəngli border (kateqoriyaya görə: emerald/sky/violet/amber/...)
- Şəkilli variant: hover zoom, gradient overlay
- Şəkilsiz variant: təmiz layout
- "Oxu →" hover effekti
- line-clamp-2 (2 sətir kəsilmə)

### NewsGrid
- Responsive grid (1→2→3 sütun)
- Kateqoriya + axtarış filteri
- Boş vəziyyətdə "📭 xəbər yoxdur" mesajı

### Ana Səhifə (index.jsx)
- Hero: gradient banner, 8 kateqoriya statistikası
- PWA install banner
- SEO head (manifest, description)