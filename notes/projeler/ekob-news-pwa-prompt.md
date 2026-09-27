# EKOB NEWS — Full PWA Portal Prompt for Emergent.sh

## Project Overview
Build a Progressive Web App (PWA) called "EKOB NEWS" — an automated news aggregator portal with 8 categories, live market ticker, and full social media integration. The design uses green (emerald shades, primary #10b981) and silver/gray (slate shades, background #0f172a) tones matching the existing logo.

## Tech Stack
- Framework: Next.js (React) with App Router
- Styling: Tailwind CSS
- PWA: next-pwa or next-offline for service worker + manifest.json
- Data: Fetch from /api/news and /api/market-prices endpoints (FastAPI backend)
- Font: System font stack (Inter or Geist as primary)

## Page Structure

### 1. Layout (app/layout.jsx)
- Dark theme base: bg-slate-900, text-slate-200
- Custom scrollbar styling (thin, slate thumb)
- Smooth scroll behavior
- Metadata: title "EKOB NEWS — Avtomatlaşdırılmış Xəbər Portalı", theme-color #0f172a
- PWA manifest link
- Selection color: emerald-500/30

### 2. Header (sticky, top-0, z-50)
- On scroll: bg-slate-900/95 backdrop-blur-md, shadow
- Logo: 40px rounded-square with gradient emerald-400 to emerald-700, letter "E" in white bold
- Text: "EKOB" in emerald-400, "NEWS" in slate-300, subtitle "Avtomatlaşdırılmış Xəbər Portalı" in slate-500 10px
- Search input: centered, max-w-md, bg-slate-800/80 border-slate-700/50 rounded-xl, emerald focus ring, placeholder "Xəbər axtar..."
- Social icons row: Facebook 📘, Instagram 📸, TikTok 🎵, Telegram ✈️ — each 32px rounded bg-slate-800 hover emerald

### 3. Ticker Bar (full-width, below header)
- Background: gradient from slate-800 via emerald-900 to slate-800
- Height: 36px
- Left badge: "CANLI" label with green pulsing dot, bg-emerald-800/50
- Scrolling horizontal ticker: infinite loop animation (30s duration, translateX -50%)
- Each item shows: SYMBOL (bold slate-200), price (mono slate-300), change % with ▲ green or ▼ red
- Symbols: BTC, ETH, CSCO, SCHD, SOL, AAPL (can expand)
- Data source: fetch /api/market-prices every 5 seconds
- Fallback: mock data when API unavailable (random small fluctuations)

### 4. Category Navigation (sticky, z-40, below ticker)
- Background: white/5 backdrop-blur, border-b slate-700/30
- 8 categories as horizontal scrollable pills:
  1. 🌱 Yaşıl Texnologiyalar (green-tech, border-l-emerald)
  2. 🌍 İqlim Dəyişikliyi (climate, border-l-sky)
  3. 🐾 Təbiət və Heyvanlar (nature, border-l-green)
  4. ♻️ Eko-həyat tərzi (eco-lifestyle, border-l-teal)
  5. 🤖 Süni İntellekt (ai, border-l-violet)
  6. ₿ Kripto Dünyası (crypto, border-l-amber)
  7. 📊 İqtisadiyyat & Maliyyə (economy, border-l-blue)
  8. 🏛 Siyasət (politics, border-l-rose)
- Active pill: bg-emerald-600 text-white, others: slate-300 hover bg-slate-700/50
- Mobile: shows short labels (first word only on small screens)

### 5. Hero Section (shown when no category selected)
- Gradient bg: emerald-900/40 to slate-900
- Border: emerald-800/20 rounded-2xl
- Decorative: blurred emerald circle (w-64 h-64) top-right
- Title: "EKOB NEWS" large heading
- Subtitle: "Avtomatlaşdırılmış xəbər aqreqatoru. Ətraf mühit, texnologiya, iqtisadiyyat və kripto dünyasından ən son xəbərlər."
- Tags: "🟢 8 kateqoriya", "⏱ Canlı yenilənir", "📱 PWA"

### 6. News Card Component
- Article card: bg-slate-800/40 hover:bg-slate-700/40 rounded-xl border-slate-700/30
- Left border accent: 4px solid colored by category
- Image variant: 160px height, hover zoom 105%, gradient overlay from bottom
- Text variant: no image, clean layout
- Title: font-semibold text-base line-clamp-2, hover text-emerald-300
- Summary: text-sm text-slate-400 line-clamp-2
- Footer: source + date left, "Oxu →" link right
- Click: opens URL in new tab

### 7. News Grid
- Responsive: 1 column mobile, 2 columns tablet, 3 columns desktop
- Gap: 4 (1rem)
- Filters by active category (prop: category)
- Filters by search query (prop: searchQuery) — searches title and summary
- Loading state: skeleton shimmer animation
- Empty state: 📭 "Bu kateqoriyada hələ xəbər yoxdur" message
- Data: fetch from /api/news?category=X&search=Y&page=Z
- Pagination: "Daha çox" button at bottom, loads next page

### 8. Footer
- 4-column grid: Brand + Categories + Platforms + Copyright
- Brand column: small logo + description text
- Categories column: 4 category links
- Platforms column: Telegram, Facebook, Instagram, TikTok links
- Copyright: "© 2026 EKOB NEWS" + "Powered by Hermes AI & Emergent.sh"
- Border-top slate-800

## API Endpoints (Backend)

### GET /api/news
Query params: category (optional), search (optional), page (default 1), limit (default 20)
Response:
```json
{
  "data": [
    {
      "id": "string",
      "title": "string",
      "summary": "string",
      "content": "string",
      "category": "green-tech|climate|nature|eco-lifestyle|ai|crypto|economy|politics",
      "image_url": "string | null",
      "source": "string",
      "source_url": "string",
      "date": "ISO datetime",
      "views": "number"
    }
  ],
  "pagination": { "page": 1, "limit": 20, "total": 150 }
}
```

### GET /api/market-prices
Response:
```json
{
  "data": [
    { "symbol": "BTC", "price": 63452.00, "change": 2.4 },
    { "symbol": "ETH", "price": 3456.00, "change": -0.8 },
    { "symbol": "CSCO", "price": 58.72, "change": 1.1 },
    { "symbol": "SCHD", "price": 78.34, "change": 0.3 },
    { "symbol": "SOL", "price": 142.80, "change": 5.2 },
    { "symbol": "AAPL", "price": 228.15, "change": -0.5 }
  ]
}
```

## PWA Configuration
- Name: "EKOB NEWS"
- Short name: "EKOB"
- Icons: 192x192 and 512x512 (generated from logo — green gradient with "E")
- Display: standalone
- Theme color: #0f172a
- Background color: #0f172a
- Start URL: /
- Offline fallback: cached news from last session

## Animations & UX
- News cards: fade-in on scroll (translateY 10px → 0, 0.5s)
- Category hover: scale 105%, emerald glow
- Ticker: smooth infinite scroll
- Page transitions: smooth opacity
- Hover effects on all interactive elements

## Mobile Responsiveness
- Header: logo + social icons visible, search collapses to icon on mobile
- Categories: horizontal scroll with short labels
- News grid: 1 column on phones
- Ticker: full width, smaller font
- Footer: stacks vertically on mobile