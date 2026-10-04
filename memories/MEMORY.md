User is Azerbaijani speaker, wants direct no-filler Azərbaycan dilində responses. Frustrated by: formal tone, 'necə kömək edə bilərəm', questions at end of every message, robotic/客服 style, süni 'darıxdım/əla/mükəmməl'. Wants: səmimi/dost kimi, qısa 1-2 cümlə, sual only when genuinely needed, heç vaxt cümlə sonunda sual vermə.
§
User's triple-save pattern: hər dəfə yeni layihə/sistem/config haqqında məlumat verəndə, onu 1) Hermes memory-ə, 2) Obsidian vault-a (qeydler/), 3) GitHub hermes-config reposuna qeyd et. Obsidian vault həm WSL-də (/mnt/c/...), həm də hermes-config/notes/ qovluğunda sinxron saxlanılır.
§
WhatsApp botları (VPS PM2 whatsapp-agent): EANA (Hermes persona, 4 ailə üzvü) + Bizim sinif (Həsən müəllim persona, 18 şagird). Hər ikisi agent.js-də hardcoded. 2.5-4s typing delay. Audio/video/şəkil/link aktiv.
§
5 Beyin (VPS-2 77.42.37.230, Docker): Çati(GPT-4o), Gemi(Gemini-2.5flash), Depi(DeepSeek), Klodi(Claude). Meta-orchestrator. 8 upgrade. /root/5beyin-bot/.env gözləyir.
§
User səmimi, isti ünsiyyət gözləyir — "işləyirəm, nə deyirsən?" kimi soyuq qarşılama onu incitdi. Salamlaşanda sadəcə hal-əhval, əsla məşğul olduğunu bildirmə. İş haqqında danışanda birbaşa.
§
EKOB NEWS PWA PORTAL + gündəlik AI avatar videosu: emergent.sh ilə qurulur (hazırlıq mərhələsi). Telegram inteqrasiyası + 8 kateqoriya + domain planı var. HeyGen seçildi (AZ dili təsdiqləndi), D-ID alternativ. Test: mətn → HeyGen → video, sonra cron ilə avtomatik.
§
Post-merge hook (WSL): ~/hermes-config/.git/hooks/post-merge — hər git pull-da notes/→Obsidian rsync+.gitignore vault extras. VPS-də broken deyil.
§
Fight Shorts brand assets (04.10): /root/fight_shorts_assets/ — banner(1254×300), 4 intro frames, watermark, anim_logo. Contact sheet-dən vision model+PIL ilə kəsildi. User AI-gen logosunu rədd etdi.