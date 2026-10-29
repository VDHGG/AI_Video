# Các repo GitHub nên dùng để xây dây chuyền sản xuất TikTok AI Explainer

Với mục tiêu của bạn và sếp Đức, mình không khuyên tìm một repo duy nhất có thể làm tất cả. Cách hiệu quả hơn là chọn **một bộ máy dựng video, một hệ thống animation tái sử dụng và một công cụ hỗ trợ phụ đề**, sau đó dùng GPT-6 Astra cùng Cursor hoặc Antigravity để kết nối quy trình.

Mình ưu tiên các repo đáp ứng 4 tiêu chí:

- **Tái sử dụng:** làm video tiếp theo mà không phải dựng lại từ đầu.
- **AI coding agent friendly:** có thể giao cho IDE agent xây dựng, chỉnh sửa và render.
- **Kết hợp UI thật với animation:** phù hợp video hướng dẫn tính năng AI.
- **Chi phí hợp lý:** ưu tiên mã nguồn mở và chạy trên máy của bạn, hạn chế phụ thuộc API trả phí.

Sau khi tìm kiếm GitHub và tài liệu dự án, có 3 lựa chọn đáng xem xét nhất cho phần dựng video: HyperFrames, Remotion và Motion Canvas. Chúng không hoàn toàn thay thế cho nhau; mỗi cái có thế mạnh riêng. [GitHub](https://github.com/mynolix/my-hyperframes?utm_source=chatgpt.com)

## 1. Top 3 repo nên ưu tiên nhất

### 🥇 1. HyperFrames — bộ máy dựng video chính



**GitHub:** [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes?utm_source=chatgpt.com)

Đây là repo mình ưu tiên số một cho dự án của bạn.

HyperFrames biến HTML, CSS, JavaScript, media và animation thành video MP4. Repo có CLI, hệ thống component dựng sẵn và skill hướng dẫn coding agent thực hiện workflow làm video. [GitHub](https://github.com/heygen-com/hyperframes/blob/main/README.md?utm_source=chatgpt.com)

**Bạn có thể dùng nó để làm gì?**

Ví dụ video hướng dẫn một setting trong ChatGPT:

- Giây 0–3: chữ động xuất hiện, tạo hook.
- Giây 3–10: video quay màn hình thật, phóng to setting cần hướng dẫn.
- Giây 10–20: animation minh họa ý nghĩa của setting.
- Giây 20–25: caption và CTA xuất hiện.

Toàn bộ cấu trúc này có thể được chuẩn hóa thành một template.

Lần tiếp theo, bạn chỉ cần thay video quay màn hình, lời thoại, nội dung và một số thông số cảnh.

**Điểm đáng giá:** HyperFrames có sẵn catalog các thành phần như transition, title, kinetic typography, caption, biểu đồ và hiệu ứng. Điều này giúp agent không phải tự viết mọi thứ từ đầu. [GitHub](https://github.com/heygen-com/hyperframes/blob/main/README.md?utm_source=chatgpt.com)

**Cách bắt đầu:**

Trong terminal của project:

```bash
npx skills add heygen-com/hyperframes
```

Sau khi cài skill, yêu cầu coding agent tạo video thử nghiệm 5–10 giây. Lưu ý làm theo hướng dẫn hiện hành của repo nếu quy trình cài đặt đã thay đổi.

**Độ phù hợp với dự án: 10/10.**

Đây là lựa chọn đầu tiên mình sẽ thử.

---

### 🥈 2. HyperFrames Launches — học cách làm video từ sản phẩm thực tế

**GitHub:** [heygen-com/hyperframes-launches](https://github.com/heygen-com/hyperframes-launches?utm_source=chatgpt.com)

Đây là repo chứa các composition HyperFrames mã nguồn mở được dùng cho những video ra mắt sản phẩm của HeyGen. [GitHub](https://github.com/heygen-com?utm_source=chatgpt.com)

Khác với repo HyperFrames chính, repo này đáng xem vì nó cung cấp **ví dụ thực tế về cách tổ chức composition và trình bày sản phẩm bằng video**.

Bạn nên nghiên cứu:
- Cách chia cảnh và chuyển tiếp.
- Cách trình bày giao diện sản phẩm.
- Cách kết hợp typography với hình ảnh.
- Cách xây dựng một đoạn mở đầu thu hút.
- Cách tổ chức code để chỉnh sửa composition.

**Cách sử dụng hiệu quả nhất:**

1. Clone repo về máy.
2. Chọn một composition gần với phong cách muốn làm.
3. Đọc cấu trúc code và các asset.
4. Chạy thử theo hướng dẫn của repo.
5. Chỉ lấy ý tưởng hoặc thành phần cần thiết để đưa vào template của mình.

Đừng copy nguyên cả dự án rồi cố sửa tất cả. Hãy chọn một composition có cách trình bày phù hợp và biến nó thành thành phần tái sử dụng.

**Độ phù hợp: 9/10.**

Đặc biệt hữu ích khi bạn muốn video trông chuyên nghiệp hơn mà chưa có nhiều kinh nghiệm motion design.

---

### 🥉 3. Remotion — phương án thay thế nếu muốn xây hệ thống video phức tạp hơn



**GitHub:** [remotion-dev/remotion](https://github.com/remotion-dev/remotion?utm_source=chatgpt.com)

Remotion cho phép tạo video bằng React, kết hợp các công nghệ web và code để xây animation, template và hệ thống render hàng loạt. [GitHub](https://github.com/remotion-dev/remotion?utm_source=chatgpt.com)

Nó đáng cân nhắc nếu sau này bạn muốn phát triển từ vài video thử nghiệm thành một hệ thống có cấu hình tập trung, chẳng hạn:

```text
Episode configuration
        |
        v
Script + scene data
        |
        v
Reusable React components
        |
        v
Render multiple videos
        |
        v
Export MP4
```

Ví dụ, bạn định nghĩa dữ liệu của mỗi video:

```json
{
  "title": "3 setting AI bạn nên biết",
  "duration": 25,
  "scenes": [
    {
      "type": "hook",
      "text": "Bạn đã biết setting này chưa?"
    },
    {
      "type": "demo",
      "asset": "assets/screen-recording.mp4"
    },
    {
      "type": "explanation",
      "text": "Giải thích một tính năng cụ thể"
    }
  ]
}
```

Đây chỉ là ví dụ về cấu trúc dữ liệu; cần viết các React components để render nội dung này.

**Ưu điểm**
- Dễ tổ chức component và dữ liệu bằng React.
- Có thể xây dựng template phức tạp.
- Có hệ sinh thái phục vụ render hàng loạt và tạo video theo dữ liệu. [GitHub](https://github.com/remotion-dev/remotion?utm_source=chatgpt.com)

**Nhược điểm**
- Cần làm quen với React và cấu trúc của Remotion.
- Không cần thiết nếu mục tiêu hiện tại chỉ là tạo những video explainer ngắn bằng HTML/CSS/JavaScript.
- Cần xem kỹ điều khoản cấp phép của Remotion, nhất là khi dùng trong hoạt động thương mại. [GitHub](https://github.com/remotion-dev/remotion?utm_source=chatgpt.com)

**Độ phù hợp hiện tại: 7/10.**

Mình sẽ chưa chọn Remotion làm bộ máy chính nếu bạn đã quyết định thử HyperFrames. Dùng đồng thời cả hai ngay từ đầu sẽ tăng độ phức tạp mà chưa chắc đem lại lợi ích.

---

## 2. Repo hỗ trợ làm animation và visual explainer

### 4. Motion Canvas — tạo animation giải thích khái niệm

**GitHub:** [motion-canvas/motion-canvas](https://github.com/motion-canvas/motion-canvas?utm_source=chatgpt.com)

Motion Canvas gồm thư viện TypeScript để lập trình animation và một editor hỗ trợ xem trước chuyển động theo thời gian thực. Dự án hướng đến animation giải thích và đồng bộ hình ảnh với voiceover. [GitHub](https://github.com/motion-canvas/motion-canvas/blob/main/README.md?plain=1\&utm_source=chatgpt.com)

Nó phù hợp với những clip kiểu:

- Giải thích AI Agent bằng sơ đồ chuyển động.
- Minh họa cách dữ liệu đi qua một workflow.
- So sánh prompt thiếu context với prompt có context.
- Giải thích một quy trình bằng hình khối và typography.

Ví dụ, muốn giải thích một AI agent hoạt động như thế nào, bạn có thể tạo animation:

```text
User request
     |
     v
AI interprets
     |
     v
Selects a tool
     |
     v
Executes action
     |
     v
Returns result
```

Các thành phần sẽ xuất hiện theo nhịp lời thoại, thay vì chỉ hiển thị một sơ đồ tĩnh.

**Khi nào nên dùng?**

Khi phần animation trở thành yếu tố quan trọng nhất của video.

**Khi nào chưa cần?**

Nếu HyperFrames đã đáp ứng đủ nhu cầu về chữ động, callout và sơ đồ, chưa cần thêm Motion Canvas.

Đây là công cụ bổ sung hoặc một hướng thay thế, không phải dependency bắt buộc của pipeline.

---

## 3. Repo hỗ trợ quay giao diện và phụ đề

### 5. ShareX — quay màn hình thật trên Windows

**GitHub:** [sharex/sharex](https://github.com/ShareX/ShareX?utm_source=chatgpt.com)



ShareX là công cụ mã nguồn mở dành cho Windows, hỗ trợ chụp màn hình, quay video, ghi GIF và chú thích hình ảnh. [GitHub](https://github.com/sharex/sharex?utm_source=chatgpt.com)

Đối với dự án này, ShareX giải quyết một việc rất thực tế: tạo các asset giao diện thật để đưa vào video.

Ví dụ, bạn muốn làm clip hướng dẫn một setting trong ChatGPT:

1. Mở ChatGPT trên trình duyệt.
2. Chọn vùng màn hình cần ghi.
3. Quay thao tác mở phần cài đặt.
4. Lưu video vào thư mục episode.
5. Đưa video vào HyperFrames để crop, zoom và highlight.

Bạn cũng có thể chụp ảnh rồi chú thích vùng cần quan tâm.

**Điểm quan trọng:** ShareX chỉ là công cụ capture, không thay thế HyperFrames. Dùng hai công cụ này cùng nhau sẽ rõ ràng hơn việc cố làm mọi thứ trong một ứng dụng.

Repo có giấy phép GPL-3.0. Nếu sau này bạn phân phối phần mềm có tích hợp hoặc sửa đổi code ShareX, hãy kiểm tra nghĩa vụ cấp phép liên quan. Nếu chỉ sử dụng ứng dụng để quay màn hình thì tình huống khác với việc phân phối một bản sửa đổi. [GitHub](https://github.com/sharex/sharex?utm_source=chatgpt.com)

**Độ phù hợp: 9/10.**

### 6. auto-subtitles — tự động tạo phụ đề bằng Whisper

**GitHub:** [mild-rgb/auto-subtitles](https://github.com/mild-rgb/auto-subtitles?utm_source=chatgpt.com)

Repo này tự động chuyển giọng nói thành phụ đề bằng faster-whisper, sau đó sử dụng FFmpeg để tạo file phụ đề hoặc xuất video có phụ đề. Nó hỗ trợ các ngôn ngữ mà Whisper nhận dạng được. [GitHub](https://github.com/mild-rgb/auto-subtitles?utm_source=chatgpt.com)

Workflow dự kiến:

```text
Voiceover.wav
      |
      v
Whisper transcription
      |
      v
SRT subtitle file
      |
      v
Review and correct text
      |
      v
Use captions in video
```

**Vì sao mình chọn repo này?**

- Có thể chạy cục bộ.
- Không nhất thiết phải dùng API trả phí để nhận dạng giọng nói.
- Có thể tạo file `.srt` để kiểm tra và chỉnh sửa.
- Hỗ trợ GPU NVIDIA tương thích, hoặc có thể chạy trên CPU với tốc độ thấp hơn. [GitHub](https://github.com/mild-rgb/auto-subtitles?utm_source=chatgpt.com)

Tuy nhiên, đây không phải công cụ tạo phụ đề karaoke hoặc typography cao cấp hoàn chỉnh. Đối với phong cách TikTok của bạn, nên dùng nó để tạo bản phụ đề ban đầu, sau đó để HyperFrames chịu trách nhiệm trình bày caption và animation.

Ngoài ra, cần thử với voiceover tiếng Việt thực tế để kiểm tra chất lượng nhận dạng trước khi đưa vào dây chuyền chính.

**Độ phù hợp: 8/10.**

---

## 4. Bảng tổng hợp: nên lấy repo nào?

| Repo | Nhiệm vụ | Ưu tiên | Có cần ngay? |
|---|---|---:|---|
| HyperFrames | Dựng và render video | 1 | Có |
| HyperFrames Launches | Tham khảo composition thực tế | 2 | Nên |
| Remotion | Xây video template bằng React | 3 | Chưa |
| Motion Canvas | Animation giải thích nâng cao | 4 | Chưa |
| ShareX | Quay UI thật, chụp screenshot | 5 | Có thể dùng ngay |
| auto-subtitles | Tạo phụ đề từ voiceover | 6 | Sau khi dựng bản đầu |

**Khuyến nghị:** không clone cả 6 repo. Chỉ cần dùng HyperFrames làm bộ máy chính, ShareX làm công cụ capture, tham khảo HyperFrames Launches và cân nhắc auto-subtitles khi cần.

---

# 5. Kiến trúc mình đề xuất cho dây chuyền TikTok

Đây là cách mình sẽ kết hợp các repo trên thành một hệ thống có thể phát triển dần.

```text
                 GPT-6 Astra
                     |
           Research + Script + QA
                     |
                     v
              Episode package
          script.md + scenes.json
                     |
          +----------+----------+
          |                     |
          v                     v
    ShareX capture        Voiceover audio
    Real product UI             |
          |                     v
          |              auto-subtitles
          |                     |
          +----------+----------+
                     |
                     v
                HyperFrames
                     |
          +----------+----------+
          |                     |
          v                     v
    Real UI footage       Motion graphics
          |                     |
          +----------+----------+
                     |
                     v
                Render MP4
                     |
                     v
                Human QA
                     |
                     v
               Approved clip
```

GPT-6 Astra là công cụ hỗ trợ nghiên cứu, viết nội dung và phát triển code. HyperFrames mới là phần chịu trách nhiệm dựng video.

Nếu muốn tích hợp tự động bằng API, cần xác minh cách truy cập model và khả năng tương thích cụ thể. Không nên mặc định rằng tên model được chọn trong giao diện ChatGPT đồng nghĩa với việc có thể gọi model đó từ API.

## 6. Cấu trúc project nên dùng

```text
ai-explainer-factory/
├── README.md
├── STYLE_GUIDE.md
├── template/
│   ├── hook/
│   ├── demo/
│   ├── explanation/
│   ├── captions/
│   └── end-card/
├── episodes/
│   ├── 001-chatgpt-privacy/
│   │   ├── research.md
│   │   ├── script.md
│   │   ├── scenes.json
│   │   ├── assets/
│   │   └── voiceover/
│   └── 002-ai-agents/
│       ├── research.md
│       ├── script.md
│       ├── scenes.json
│       └── assets/
└── exports/
    ├── previews/
    └── final/
```

Đây là cấu trúc logic đề xuất. Khi khởi tạo HyperFrames, cần điều chỉnh các thư mục và file composition theo quy ước thực tế của framework.

### Điều quan trọng nhất

Đừng để mỗi episode trở thành một project code riêng.

Thay vào đó, hãy tách:

- **Template:** màu sắc, font, animation, transition, caption, end card.
- **Episode:** script, video UI, voiceover, nguồn tham khảo và nội dung từng cảnh.

Như vậy, khi sếp yêu cầu thêm một clip tips mới, bạn không phải bắt đầu từ số 0.

---

# 7. Kế hoạch triển khai thực tế

## Giai đoạn 1 — Chứng minh render hoạt động

Mục tiêu: tạo video 5 giây bằng HyperFrames.

1. Kiểm tra Node.js và FFmpeg.
2. Cài HyperFrames theo tài liệu chính thức.
3. Tạo composition đầu tiên.
4. Thêm chữ động và một background.
5. Render MP4.
6. Mở file và kiểm tra kết quả thực tế.

Repo chính: [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes?utm_source=chatgpt.com)

## Giai đoạn 2 — Xây template hoàn chỉnh

Tạo các component có thể tái sử dụng:

- `HookScene`
- `ProductDemoScene`
- `ExplanationScene`
- `Caption`
- `Callout`
- `EndCard`

Nghiên cứu cách tổ chức composition trong repo ví dụ: [heygen-com/hyperframes-launches](https://github.com/heygen-com/hyperframes-launches?utm_source=chatgpt.com)

## Giai đoạn 3 — Sản xuất clip đầu tiên

Chủ đề: **“Bạn dùng ChatGPT mỗi ngày? Kiểm tra setting này.”**

1. Xác minh nội dung bằng tài liệu chính thức.
2. Quay giao diện thật bằng ShareX.
3. Viết voiceover dài khoảng 20–30 giây.
4. Dùng template để dựng.
5. Kiểm tra phụ đề, âm thanh và độ dễ hiểu.
6. Xuất video và đưa sếp duyệt.

## Giai đoạn 4 — Kiểm tra khả năng tái sử dụng

Tạo clip thứ hai bằng chính template đó.

Nếu vẫn phải sửa nhiều code hoặc viết lại cấu trúc composition, cần đơn giản hóa hệ thống trước khi tự động hóa thêm.

---

# 8. Một lưu ý quan trọng về license và chi phí

Mã nguồn mở không đồng nghĩa mọi thành phần đều miễn phí trong mọi trường hợp sử dụng.

- HyperFrames: repo chính công bố giấy phép Apache 2.0. [GitHub](https://github.com/heygen-com/hyperframes/blob/main/README.md?utm_source=chatgpt.com)
- Motion Canvas: repo chính công bố giấy phép MIT. [GitHub](https://github.com/motion-canvas?utm_source=chatgpt.com)
- Remotion: có điều khoản cấp phép riêng, cần xem xét nếu sử dụng thương mại. [GitHub](https://github.com/remotion-dev/remotion?utm_source=chatgpt.com)
- ShareX: GPL-3.0. [GitHub](https://github.com/sharex/sharex?utm_source=chatgpt.com)

Ngoài giấy phép, chi phí thực tế có thể đến từ API, TTS, dịch vụ render cloud hoặc các asset trả phí. Với prototype, mình đề xuất chạy cục bộ và chưa sử dụng dịch vụ cloud có tính phí nếu chưa cần.

---

## Kết luận: nếu là mình, mình sẽ bắt đầu với đúng 3 repo

**1. HyperFrames:** bộ máy dựng video chính.

**2. HyperFrames Launches:** nguồn tham khảo cách xây composition đẹp.

**3. ShareX:** quay giao diện thật để tạo asset cho video.

Sau khi dựng được clip đầu tiên, mới quyết định có cần thêm repo tạo phụ đề tự động hay công cụ animation chuyên sâu hay không.

**Mục tiêu cuối cùng không phải là sưu tầm repo GitHub. Mục tiêu là có một template mà bạn có thể giao cho coding agent: nhập chủ đề, cung cấp giao diện thật và script đã duyệt, rồi tạo ra một clip mới mà không phải xây dựng lại toàn bộ từ đầu.**