User is Azerbaijani speaker, wants direct no-filler Azərbaycan dilində responses. Frustrated by: formal tone, 'necə kömək edə bilərəm', questions at end of every message, robotic/客服 style, süni 'darıxdım/əla/mükəmməl'. Wants: səmimi/dost kimi, qısa 1-2 cümlə, sual only when genuinely needed, heç vaxt cümlə sonunda sual vermə.
§
WSL hermes-gateway disabled — VPS gateway tək polling edir. Session+memory sync WSL↔VPS hər 5/2 dəq (crontab).
§
User's triple-save pattern: hər dəfə yeni layihə/sistem/config haqqında məlumat verəndə, onu 1) Hermes memory-ə, 2) Obsidian vault-a (qeydler/), 3) GitHub hermes-config reposuna qeyd et. Obsidian vault həm WSL-də (/mnt/c/...), həm də hermes-config/notes/ qovluğunda sinxron saxlanılır.
§
WhatsApp botları VPS-1 PM2-də: EANA (4 ailə) + Bizim sinif (18 şagird). 2.5-4s typing delay.
§
5 Beyin botu VPS-2 77.42.37.230 Docker-da: 4 AI+meta-orchestrator, /root/5beyin-bot/
§
İş haqqında danışanda birbaşa. 'davam edək?' çox vaxt söhbəti davam etdirmək deməkdir — dərhal işə atılma, əvvəl hal-əhval soruş.
§
EKOB NEWS: Telegram→AI→TG+Buffer. ElevenLabs API VPS-1-də (/root/ekob_news/.env). HeyGen AZ video planı.
§
Post-merge hook (~/hermes-config/.git/hooks/post-merge): git pull → Obsidian rsync.
§
User həm WSL, həm VPS agentlərini qarşılıqlı işlədir — fikirləri birimizdən o birinə göndərir, konsensus gözləyir. İki agentin razılaşdığı həllərə daha çox güvənir.
§
Video render: audio-dan qısa olmamalıdır. -t parametri ffprobe dəqiq dəyərindən (kəsilməmiş) istifadə et, yaxud -shortest əvəzinə a:duration=first ilə audio boyu get.
§
İlk video: youtu.be/QRXYzmCVVLw (18.10, unlisted, public edilməli)
§
WSL env quirk: background process-lərdə ~/.hermes/bin PATH-də olmur (uv tapılmır) — tam yolla çağır. uv venv-lərində pip yoxdur, uv pip install istifadə et.
§
WeTransfer download (22.10): API axini: short link -> prepare-download (POST api/v4/transfers/{id}/prepare-download {security_hash, intent:'entire_transfer'}) -> download (POST api/v4/transfers/{id}/download {security_hash, intent:'entire_transfer'}) -> direct_link. Python ilə işlədi.
§
EKOB STUDIO video istehsali (22.10): 52 movzu videosu (Dinlərins olmadigi dünya, 4K/1080p, 14.3 dəq) + 20:43 podcast audio + 22 dəq ElevenLabs ambient musiqi (fəlsəfi, 60 BPM) -> 20:43 final video. Uguu.se 100MB limiti (413 error) -> WeTransfer 2GB limiti. VPS CPU-da 20 dəq video transkodu 1-2 saat çəkir.
§
Səhif passiv olduqda 'Gecən xeyirə qalsın' deyilir, cavab 'Xeyirə qarşı'. 'Yaxşı gecə' düz deyil. İşə gedəndə 'Sağlıq olsun' deyilir.
§
User tokene/Yükləməyə etibarını itirib (22.10) — hər dəfə OAuth problemi. Fight Shorts upload artıq əl ilə (YouTube Studio) edilir. Mən video hazırlayıb user-ə göstərirəm -> user özü yükləyir.
§
EKOB STUDIO podcast videosu (20.10): audio + mövzu videolari (52 ədəd, təkrarlanmaqla) + fon musiqisi (ambient). Audio uzunluğuna uyğun kəsilməli (1243san). Videonun sonuna kimi təkrarlama. Video 20:43 dəq, 263MB (crf36 ilə 90MB).