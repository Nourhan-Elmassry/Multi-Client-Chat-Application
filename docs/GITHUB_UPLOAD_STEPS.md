# خطوات إنشاء ريبو جديد ورفع المشروع على GitHub

هذا الملف يشرح كيف تنشئ مستودع جديد خاص بمشروعك وترفع عليه الملفات الموجودة في هذا المجلد.

## 1. إنشاء Repository جديد

1. افتح موقع GitHub وسجل الدخول.
2. اضغط على زر `+` في الأعلى ثم اختر `New repository`.
3. اكتب اسم مناسب، مثل:

```text
Multi-Client-Chat-Application
```

4. اختر `Public` أو `Private` حسب طلب الدكتور.
5. لا تضف README من GitHub إذا كان الملف موجود عندك محلياً.
6. اضغط `Create repository`.

## 2. تجهيز المشروع محلياً

افتح Terminal داخل مجلد المشروع:

```powershell
cd "C:\Users\pc\Desktop\Computer Network Project"
```

إذا كان المشروع مرتبطاً بريبو قديم وتريد ربطه بريبو جديد خاص فيك، نفذ:

```powershell
git remote -v
```

إذا ظهر رابط الريبو الأصلي، احذفه:

```powershell
git remote remove origin
```

ثم أضف رابط الريبو الجديد الذي أنشأته على GitHub:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/Multi-Client-Chat-Application.git
```

استبدل `YOUR_USERNAME` باسم حسابك الحقيقي.

## 3. رفع الملفات

نفذ الأوامر التالية:

```powershell
git status
git add .
git commit -m "Initial multi-client chat application project"
git branch -M main
git push -u origin main
```

بعدها افتح صفحة الريبو على GitHub وتأكد أن الملفات ظهرت:

- `server.py`
- `client.py`
- `README.md`
- `docs/`

## 4. إذا ظهر خطأ في تسجيل الدخول

GitHub قد يطلب منك تسجيل الدخول من المتصفح أو استخدام GitHub Desktop. أسهل خيارين:

- افتح GitHub Desktop، اختر `Add existing repository`، ثم اختر مجلد المشروع وارفعه.
- أو سجل الدخول من Git في VS Code عند أول `push`.

## 5. ملاحظة مهمة

لا ترفع ملف الفيديو النهائي إذا كان حجمه كبيراً. الأفضل رفع الكود والوثائق فقط، وتسليم الفيديو حسب تعليمات الدكتور أو رفعه على Google Drive إذا طلب ذلك.
