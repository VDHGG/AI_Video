# HyperFrames — Prompt dựng video DB Index v7

> **Cách dùng:** Đưa file `DB_INDEX_V7_REVIEWED_STORYBOARD.md` cho AI coding agent đang có bộ skill HyperFrames (ví dụ Codex/Claude Code/Cursor), rồi dán nguyên prompt này. Nếu không thể đính kèm file, các câu dải dưới và timecode đã có đầy đủ trong prompt bên dưới.

```text
/hyperframes

TASK: Build the final proposed v7 of a Vietnamese vertical, silent animated explainer about database indexes, based on the attached DB_INDEX_V7_REVIEWED_STORYBOARD.md. This is a revision of an existing v5 aesthetic, not a brand-new aesthetic. If the actual v5 project/composition is available, reuse its structure, objects, layout, colors, motion assets and typography; selectively replace copy, fix misleading labels, and improve storytelling according to v7. If v5 is not available, build a faithful 2D motion-graphics composition from the v7 storyboard. Never claim that you inspected v5 unless it is actually present.

VIDEO SPECS — HARD REQUIREMENTS
- Exactly 110.0 seconds, 1080x1920 (9:16 vertical), 60 fps.
- Silent: no music, voiceover, TTS or sound effects.
- Font: Be Vietnam Pro Bold, correct Vietnamese accent rendering.
- Lower-third subtitle font: 45px; max 2 lines, width <=936px, x centered, top around y=1148, line-height 1.28. Absolute safe boundaries: no text in y<168 and no text at y>1330.
- Other labels >=28px. End CTA typography remains 52/64/40px as specified.
- Keep the original palette: ivory #f4f1ea, gold #e7c56a, teal #7dcec4, orange #e07a5f, inactive #9a9388, cells #1c2430, dark background family #0c0f14.
- Keep 6 scenes and absolute timing: S1 0-16, S2 16-40, S3 40-60, S4 60-84, S5 84-102, S6 CTA 102-110.
- Lower captions animate word-by-word, with role-specific highlights; no per-letter random motion. Every sentence must stay within two lines; do not silently reduce font below 45px.
- Treat the on-screen Vietnamese text listed here as exact strings: do not paraphrase or translate.

EXACT LOWER CAPTION TRACK (17 beats; no lower caption during CTA)
0.0-5.0: Cần tìm tên? Mở đúng chữ cái, khỏi lật cả danh bạ.
5.0-10.0: Trong bảng dữ liệu, ta cũng cần tìm dòng thuộc nhóm 7.
10.0-16.0: Index chỉ tới dòng phù hợp, thay vì dò từng dòng.
16.0-22.0: Chưa có Index: đếm nhóm 7 mất 1,3 ms.
22.0-28.0: Có Index: cùng phép đếm chỉ còn 0,04 ms.
28.0-34.0: Hai số là lần ở giữa của 9 lần đo.
34.0-40.0: Đọc nhanh hơn. Nhưng thêm dòng mới lại tốn việc hơn.
40.0-46.6: Mỗi lần thêm dòng, máy còn phải cập nhật Index.
46.6-53.2: Ghi 8.000 dòng trong bộ nhớ: từ 5,2 lên 8,2 ms.
53.2-60.0: Index còn chiếm thêm khoảng 460 KB trên đĩa.
60.0-66.0: Bảng ít dòng? Quét hết cũng có thể đã đủ nhanh.
66.0-72.0: Cột có rất ít giá trị khác nhau? Đừng vội thêm Index.
72.0-78.0: Ghi hoặc sửa liên tục? Index cũng phải cập nhật theo.
78.0-84.0: Ít truy vấn dùng cột đó? Index có thể không đáng.
84.0-90.0: Bắt đầu từ cột bạn hay dùng để lọc dữ liệu.
90.0-96.0: Hoặc cột dùng để ghép hai bảng, rồi kiểm tra lại.
96.0-102.0: Index không miễn phí. Hãy đo cả lúc đọc lẫn lúc ghi.


OPTIONAL MANUAL 2-LINE BREAKS — use these exact semantic breakpoints when rendering captions; each pair concatenates to the exact caption above. Do not split a word, number, or the phrase "chữ cái":
0-5: "Cần tìm tên?" / "Mở đúng chữ cái, khỏi lật cả danh bạ."
5-10: "Trong bảng dữ liệu," / "ta cũng cần tìm dòng thuộc nhóm 7."
10-16: "Index chỉ tới dòng phù hợp," / "thay vì dò từng dòng."
16-22: "Chưa có Index:" / "đếm nhóm 7 mất 1,3 ms."
22-28: "Có Index:" / "cùng phép đếm chỉ còn 0,04 ms."
28-34: "Hai số là lần ở giữa" / "của 9 lần đo."
34-40: "Đọc nhanh hơn." / "Nhưng thêm dòng mới lại tốn việc hơn."
40-46.6: "Mỗi lần thêm dòng," / "máy còn phải cập nhật Index."
46.6-53.2: "Ghi 8.000 dòng trong bộ nhớ:" / "từ 5,2 lên 8,2 ms."
53.2-60: "Index còn chiếm thêm" / "khoảng 460 KB trên đĩa."
60-66: "Bảng ít dòng?" / "Quét hết cũng có thể đã đủ nhanh."
66-72: "Cột có rất ít giá trị khác nhau?" / "Đừng vội thêm Index."
72-78: "Ghi hoặc sửa liên tục?" / "Index cũng phải cập nhật theo."
78-84: "Ít truy vấn dùng cột đó?" / "Index có thể không đáng."
84-90: "Bắt đầu từ cột bạn hay dùng" / "để lọc dữ liệu."
90-96: "Hoặc cột dùng để ghép hai bảng," / "rồi kiểm tra lại."
96-102: "Index không miễn phí." / "Hãy đo cả lúc đọc lẫn lúc ghi."

SCENE VISUAL BEATS
S1: Open a Vietnamese alphabetical address book with tabs A, Đ, M, N. Hook at 0s: teal 'INDEX: TÌM NHANH' versus orange 'NHƯNG GHI CHẬM?'. At 5s morph to an 8-row illustrative table with filter 'nhóm = 7'. Sequential scan first; at 10s the Index beam jumps to two matching rows. Permanent legible label: 'SƠ ĐỒ MINH HỌA', followed by '8 dòng · 2 khớp'. Never claim this is the benchmark dataset.
S2: Split left/right, SAME query 'nhóm = 7'. Dataset label 'BẢNG THỬ: 50.000 dòng · 500 dòng nhóm 7'. LEFT 'CHƯA CÓ INDEX' sequential scan and big gold '1,3 ms'; RIGHT 'CÓ INDEX' jump and big gold '0,04 ms'. Gold source detail at 28-34s 'Lần ở giữa · 9 lần đo' and smaller 'Đã bỏ lượt làm nóng'. Transition at 34s by introducing a new row and changing emphasis from teal to orange.
S3: Animate insert into table, then second operation updates Index. At 46.6s compare 'Chưa có Index · 5,2 ms' (teal) versus 'Có Index · 8,2 ms' (orange), with label 'Ghi 8.000 dòng · trong bộ nhớ'. At 53.2s show a disk / file growing by '≈460 KB', label 'Bảng thử 50.000 dòng'. Do not imply these in-memory timings are disk writes.
S4: Title 'ĐỪNG VỘI THÊM INDEX KHI…'. Four successive concise diagrams: small table, many duplicated group values, frequent group update, query asking note instead of nhóm. Display accumulating items: 'Bảng ít dòng'; 'Nhiều dòng trùng giá trị'; 'Cột bị ghi/sửa thường xuyên'; 'Ít truy vấn cần cột đó'. Do NOT say 'Index đứng yên'.
S5: Title 'CỘT NÀO ĐÁNG THỬ?'. Show filter query 'nhóm = 7', then two tables joined at a shared group, then concise takeaway 'ĐO LÚC ĐỌC' (teal) and 'ĐO LÚC GHI' (orange), centered gold 'CÓ ĐÁNG KHÔNG?'. Do not show 'join'; use 'ghép'.
S6 (102.0-110.0): Exactly this CTA, broken across 3 visual lines:
  Line 1 'Hãy Follow' at 52px
  Line 2 'Anh 40 học AI' at 64px, GOLD, appears at ~103.2s
  Line 3 'để cập nhật nhiều thông tin về AI hơn.' at 40px, appears at ~105.5s
  Full literal sentence is: 'Hãy Follow Anh 40 học AI để cập nhật nhiều thông tin về AI hơn.'
  No buttons, hashtags, fourth line, or additional audio.

TECHNICAL IMPLEMENTATION AND QUALITY CONTROLS
- Author a deterministic HTML/CSS/GSAP-based HyperFrames composition; register GSAP timelines in window.__timelines, use timed .clip elements with data-start, data-duration, data-track-index, and do not use Math.random() or async animation setup. Ensure accurate seeking/frame rendering.
- Use purposeful motion only: scan moves through all rows, jump goes straight to matches, Index updates after the inserted row. Avoid glitch effects, heavy particles, gratuitous zoom, busy 3D, or perpetual animation.
- Gold is for numbers and questions, teal for read benefits, orange for scanning or update costs. Avoid flooding the entire canvas with highlights.
- Avoid graph misinformation: either make comparison bars mathematically proportional OR make it evident they are conceptual; never label an inaccurate bar chart as to-scale.
- No additional statistics, fabricated speedups, claims about universal DB behavior, or invented benchmark conditions.
- Before final export, lint, preview and check text overflow/occlusion, especially Vietnamese accents. Inspect key frames at 0,4,10,15,20,25,31,37,44,50,56,63,69,75,81,87,93,99,104,109 seconds. If any subtitle wraps to 3 lines, adjust manual line breaks and widths, NOT font size.
- Render MP4 and report the verified duration, size, fps, no-audio status, and all deviations from this specification.
```

## Nguồn tài liệu kỹ thuật HyperFrames

- Tài liệu prompting: https://hyperframes.app/docs/3-guides/2-prompting
- Quickstart: https://hyperframes.app/docs/1-startup/2-quickstart
- Tổng quan kỹ thuật: https://hyperframes.app/docs/1-startup/1-introduction

**Lưu ý:** Prompt này hướng đến **HyperFrames của HeyGen** (HTML/CSS/JS/GSAP, dựng thông qua coding agent). Nếu bạn dùng sản phẩm **Hyperframe.ai** khác tên tương tự, hãy giữ storyboard và copy nhưng bỏ phần chi tiết về CLI/GSAP.
