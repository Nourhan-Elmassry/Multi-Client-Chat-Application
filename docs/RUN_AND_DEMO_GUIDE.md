# خطوات التشغيل وسيناريو الديمو

## البرنامج المقترح

استخدم واحد من هذه الخيارات:

- VS Code مع Terminal مدمج.
- Windows Terminal.
- PowerShell.
- PyCharm Terminal.

الأفضل للتصوير: VS Code لأنه يسمح لك تعرض الملفات والكود والـ Terminal في نفس الشاشة.

## المتطلبات

تأكد أن Python مثبت:

```powershell
python --version
```

إذا لم يعمل الأمر، جرب:

```powershell
py --version
```

## فتح مجلد المشروع

في PowerShell أو Terminal:

```powershell
cd "C:\Users\pc\Desktop\Computer Network Project"
```

## تشغيل السيرفر

افتح Terminal أول وشغل:

```powershell
py server.py
```

إذا كان أمر `python` يعمل على جهازك، يمكنك أيضاً استخدام:

```powershell
python server.py
```

المتوقع أن ترى رسالة مثل:

```text
[STARTED] Server is running on 127.0.0.1:5000
[WAITING] Waiting for clients to connect...
```

## تشغيل أول Client

افتح Terminal ثاني داخل نفس المجلد:

```powershell
py client.py
```

عند السؤال عن الاسم اكتب:

```text
Ahmad
```

## تشغيل ثاني Client

افتح Terminal ثالث:

```powershell
py client.py
```

عند السؤال عن الاسم اكتب:

```text
Sara
```

## سيناريو الديمو أثناء تصوير الفيديو

1. اعرض `server.py` بسرعة واشرح أن السيرفر يستخدم `socket` و `threading`.
2. شغل السيرفر.
3. شغل أول Client باسم `Ahmad`.
4. شغل ثاني Client باسم `Sara`.
5. من نافذة Ahmad اكتب:

```text
Hello Sara
```

6. وضح أن Sara استقبلت:

```text
Ahmad: Hello Sara
```

7. من نافذة Sara اكتب:

```text
Hi Ahmad
```

8. وضح أن Ahmad استقبل:

```text
Sara: Hi Ahmad
```

9. من نافذة Sara اكتب:

```text
/exit
```

10. ارجع لنافذة السيرفر واشرح أن السيرفر لم يتوقف، بل حذف Sara من قائمة العملاء المتصلين واستمر بالعمل.

## ترتيب الشاشة المقترح للتصوير

- اليسار: VS Code وفيه `server.py` أو `client.py`.
- اليمين: ثلاث نوافذ Terminal صغيرة:
  - Server
  - Client Ahmad
  - Client Sara

## نقاط احكيها أثناء الديمو

- السيرفر هو نقطة الاتصال المركزية.
- كل Client يتصل بالسيرفر باستخدام TCP socket.
- لكل Client Thread خاص على السيرفر.
- الرسالة لا تذهب مباشرة من Client إلى Client، بل تمر عبر السيرفر.
- السيرفر يستخدم `broadcast()` لإرسال الرسالة لجميع العملاء الآخرين.
- أمر `/exit` يثبت أن الخروج لا يسبب انهيار السيرفر.

## مشاكل شائعة

إذا ظهر:

```text
[ERROR] Could not connect to the server
```

فهذا يعني أنك شغلت `client.py` قبل `server.py`.

ملاحظة على هذا الجهاز: اختبار التشغيل نجح باستخدام `py`، لذلك استخدم `py server.py` و `py client.py` أثناء التصوير.

إذا ظهر خطأ أن المنفذ مستخدم، أغلق السيرفر القديم أو غيّر قيمة `PORT` في `server.py` و `client.py` لنفس الرقم.
