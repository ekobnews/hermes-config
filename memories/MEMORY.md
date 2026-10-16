User is Azerbaijani speaker, wants direct no-filler Azərbaycan dilində responses. Frustrated by: formal tone, 'necə kömək edə bilərəm', questions at end of every message, robotic/客服 style, süni 'darıxdım/əla/mükəmməl'. Wants: səmimi/dost kimi, qısa 1-2 cümlə, sual only when genuinely needed, heç vaxt cümlə sonunda sual vermə.
§
User's triple-save pattern: hər dəfə yeni layihə/sistem/config haqqında məlumat verəndə, onu 1) Hermes memory-ə, 2) Obsidian vault-a (qeydler/), 3) GitHub hermes-config reposuna qeyd et. Obsidian vault həm WSL-də (/mnt/c/...), həm də hermes-config/notes/ qovluğunda sinxron saxlanılır.
§
Post-merge hook (WSL): ~/hermes-config/.git/hooks/post-merge — hər git pull-da notes/→Obsidian rsync+.gitignore vault extras. VPS-də broken deyil.
§
Fight Shorts (06.10): 25 klip kitabxana (4 dovuscu), 17 iri musiqi (Clash Defiant stili). Story arc (3 hisse + yazi). Ses cixarildi (robotik). Slo-mo texire (ML/GPU lazim). Cron: 1/video/gun 18:00 AZ, kitabxana→Dailymotion fallback. YouTube VPS IP bot-blok.
§
5 Beyin (04.10): Klodi claude-sonnet-4-20250514→sonnet-5, Depi deepseek-chat→flash (ikisi retired idi). Video intro cixarildi (piksel). Conor yuklendi. Yalniz watermark qaldi.
§
User: "Mən işimi getdikcə peşəkar hala gətirməyə çalışıram" — wants discussion first, then action. Wants quality roadmap guidance (nəyi hansı sırada peşəkarlaşdıraq). Sharp eye for quality — rejected pixelated intro, boring music. Likes aggressive fight music (Clash Defiant type). Before any action, discuss (müzakirə) — never implement without user confirming.
§
Fight Shorts (08.10): 25 video kitabxana + 17 musiqui local. Story arc 3 hisse (STAGE/BATTLE/CHAMPION) yazi overlay. Ses cixarildi (robotik, Voice Lab lazim). Slo-mo yox (ML/GPU yox). Cron 1/gun 18:00 AZ 60-75s. YouTube VPS IP bot-blok → Dailymotion fallback.
§
User wants ritmik/aqressiv beat-heavy music (Hackbeat/Raving Energy style), NOT orchestral/epic. Hard gym/training beats. Musiqi problemi hele hell olunmayib (SoundCloud/Uppbeat/YouTube blok). 5 Beyin bot vison duzeldi (test gozlenir). Hәftәlik Best Of (cume 18:00 AZ) quruldu.
§
User approval flow (08.10): video once preview, after approval upload. Formula: Dailymotion fight clip + electronic/beat music (Zap Beat style) = best results. 5 Beyin: image reading vision API (Cati/Gemi/Klodi), dil prompt "YALNIZ Azerbaycan". Music: 24 electronic/beat tracks, old orkestral silindi. Time awareness: user wants me to know saat/gece/sabah.
§
Video onay flow: goster, sonra yukle. Zap Beat musiqu stili. Dailymotion dovus clip + elektron musiqu = Elbrus cox beyendi (Ngannou).
§
User wants NO Kevin MacLeod music ever (Zap Beat style only). ElevenLabs Music API available on existing $5/mo Starter plan — check existing paid services before suggesting new ones (lesson: suggested Suno AI before checking ElevenLabs, user corrected me).
§
Musiqi helli: ElevenLabs Music API (Starter $5/ay oturdu, artiq hec bir elave xerc yox). Kevin MacLeod silindi. Her short ucun orijinal AI musiqi yaranir - hec vaxt tekrarlanmir, claim yox. Pipeline auto_shorts.py-de yenilendi.
§
Fight Shorts keyfiyyət (14.10): Yalnız vizual yoxlanmış (clip_verdicts.json, gemini) DöYÜŞ klipləri seçilir — müsahibə/trash talk klipi RƏDD. Montaj: rəng korreksiyası + Ken Burns zoom + loudnorm(-14LUFS) + fade in/out + yuv420p + faststart (Telegram səbəbi). ElevenLabs musiqi prompt: 145BPM 3 hissəli ark. YouTube OAuth: Web client 'Fight Shorts Web' (desktop işləməz, redirect_uri=developers.google.com/oauthplayground — /oauth2 DEYİL!).
§
Proxy: Decodo rezidensial (gate.decodo.com:10001, $4/GB PAYG, limit bitdi). 46 klip kitabxana (anderson-silva 4, canelo 8, conor 9, jon-jones 11, khabib 8, ngannou 6). ElevenLabs Music API ses+musiqi. Kevin MacLeod tarix. Həftə ici Mon-Fri 20:00 AZ review+upload. Senbə 20:00 AZ heftelik analiz. Həftə sonu istirahət. Video archive: /root/fight_shorts_review/. OAuth yenilendi (14.10): client Fight Shorts Web (Web application), refresh token taze. Scope: yalniz youtube.upload. Tyson Fury yuklendi Kr9ERoQGgXY. Vision: auxiliary.vision.provider=openrouter, model=gemini-2.5-flash. Video encode: pix_fmt yuv420p + movflags faststart.
§
Elbrus 👊 emojisindən imtina etdi (08.10): Heç vaxt, heç bir yazının sonunda 👊, 😄, gülüş/əlcək emojisi qoyma. Defələrlə xəbərdarlıq edib, məyus olub. Bu, KESİN qaydadır.
§
OpenRouter balans: $9.73 (11.10.2026, user artirdi). $2 monitor cron qurulub. Vision provider yoxdur — "hermes setup" teleb edir.
§
Vizual analiz: auxiliary.vision.provider=openrouter, model=google/gemini-2.5-flash (config.yaml). Coəxdis düzəldildi (hər şəkil xəta verirdi). YouTube OAuth: yeni Web client (ID: 977493157543-o328j3ipjj223533loa8h4p360b6vqad, Secret: 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). Playground redirect URI: https://developers.google.com/oauthplayground (without /oauth2). Köhnə token revoke olunub.
§
Video encoding: shorts videolar ucun mütləq pix_fmt yuv420p + movflags +faststart istifadə et. 4:4:4/yuv444p formatı Telegram Desktop-da acilmir (Video.Unsupported.Desktop). Həmçinin avtomatik video hazırlayanda hər günün faylını ayri saxla üstune yazma.
§
Daima əvvel şənədiy xidmətləri yoxla (ElevenLabs, ödənilən) yənixərc təklif etməzdən.
§
Skill library yenilənməsi (15.10): youtube-shorts-production (ElevenLabs .env cron fix + slug parsing hatası) + humanizer (user-specific corrections: emoji ban, birbaşa üslub, sual qadağası, vaxt məlumatı, AZ dili). hər iki referans yeniləndi.
§
YouTube Shorts limit (15.10): Copyright bloku >60san. Khabib 66san bloklandi. Pipeline max 60san (tehlukesizlik 58san). Shorts-da copyrigt qorunan mezmun 60san-dan uzun ola bilmez.
§
Khabib yuklendi 15.10 hjn6UI_R0p4 (copyright bloklandi, 66san). Conor dublikat WiEiKNyhabE (copy of 05.10 video). Schedule: anderson-silva next, sonra cycle restart. User: silmek meselesini boş ver.
§
Keyfiyyet (15.10 tesdiqlendi): contrast 1.08, saturation 1.22, Ken Burns zoom 1.06, loudnorm -14, fade in/out, musiqi prompt 145BPM 3 hisse (intro→buildup→drop). Clip secimi: gemini vizual yoxlama, yalniz DOYUS. User video and music quality-dan memnun (nehayet istediyim dereceye yaxinlasirsan).