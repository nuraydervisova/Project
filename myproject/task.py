from flask import Flask, render_template_string
app = Flask(__name__)
@app.route("/")
def about_aesma():
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>WEB SAYT</title>
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}" />
<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  body {
    background: #D8DCE2;
    color: #333;
    line-height: 1.6;
    padding: 20px;
  }
  .top-blue-line {
    width: 100%;
    height: 0.15cm;
    background-color: #1B1B7C;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 9999;
    border-radius: 3px;
  }
  .top-gray-line {
    width: 100%;
    height: 0.2cm;
    background-color: #B2B2B0;
    position: fixed;
    top: 0.1cm;
    left: 0;
    right: 0;
    z-index: 9998;
    border-radius: 3px;
  }
  .container {
    width: 100vw;
    max-width: none;
    background: #C0C5CC;
    margin: 0 auto;
    padding: 20px 10px;
    border-radius: 2px;
    box-shadow: none;
    position: relative;
  }
  .navbar {
    display: flex;
    align-items: center;
    margin-bottom: 5px;
  }
  .logo img {
    width: 100px;
    height: auto;
    margin: 45px 0 20px 30px;
    border-radius: 50px;
  }
  .center h1 {
    position: relative;
    font-size: 1.2rem;
    color: #2121BC;
    margin: -80px 0 50px 85px;
    padding: 20px 30px 10px 30px;
    text-align: left;
    line-height: 1.1;
  }
  .center p {
    display: block;
    max-width: calc(100% - 2cm);
    height: 100px;
    margin: 20px auto;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    padding-left: 1cm;
    padding-right: 1cm;
  }
  .center img {
    display: block;
    width: 100%;
    height: 11cm;
    object-fit: cover;
    margin: 20px auto;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    border-radius: 0;
  }
  .text-and-degrees {
    display: flex;
    gap: 30px;
    justify-content: space-between;
    flex-wrap: wrap;
  }
  .text-and-degrees p {
    flex: 1;
    max-width: 100%;
    line-height: 1.5;
    color: #444;
  }
  .degree-section {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    justify-content: center;
    margin-bottom: 30px;
  }
  .degree-box {
    flex: 1 1 300px;
    background-color: #E6F0FF;
    padding: 20px 25px;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(31, 95, 191, 0.3);
    position: relative;
    overflow: hidden;
  }
  .degree-box h2 {
    color: #1F5FBF;
    margin-bottom: 15px;
    font-size: 1.3rem;
    position: relative;
    z-index: 2;
  }
  .degree-box ul {
    list-style-type: disc;
    padding-left: 20px;
    position: relative;
    z-index: 2;
  }
  .degree-box ul li {
    margin-bottom: 8px;
    color: #333;
    font-weight: 600;
  }
  .small-bg {
    position: absolute;
    top: 10px;
    right: 10px;
    width: 100px;
    height: 60px;
    background-position: center;
    opacity: 0.3;
    border-radius: 5px;
    z-index: 1;
  }
  h2 {
    margin-top: 40px;
    margin-bottom: 10px;
    color: #1F5FBF;
    text-align: center;
  }
  .act-hall-section {
    display: flex;
    align-items: flex-start;
    gap: 20px;
    margin-top: 20px;
    flex-wrap: wrap;
  }
  .act-hall-section img {
    width: 400px;
    max-width: 600px;
    height: 280px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }
  .act-hall-section p {
    flex: 1;
    line-height: 1.6;
    font-size: 1rem;
    color: #333;
  }
  .footer-hours {
    background-color: #0B1A66;
    color: white;
    text-align: center;
    padding: 3px 6px;
    width: 100%;
    font-size: 0.95rem;
    margin-top: 75px;
  }
  .footer-hours h3 {
    font-size: 1.6rem;
    margin-bottom: 15px;
  }
  .footer-hours .clock-icon {
    width: 45px;
    height: 45px;
    margin-bottom: 10px;
  }
  .footer-hours ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .footer-hours ul li {
    font-size: 1.2rem;
    margin: 6px 0;
  }
  /* Responsive */
  @media (max-width: 700px) {
    .degree-section {
      flex-direction: column;
    }
    .degree-box {
      max-width: 100%;
    }
  }
</style>
</head>
<body>
  <div class="top-blue-line"></div>
  <div class="top-gray-line"></div>
  <div class="container">
    <div class="navbar">
      <div class="logo">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEvk2nEFXVYBWz9foFrN1wiuUeJ5FlKqTHaw&s" alt="AƏSMA Logo" />
      </div>
    </div>
    <div class="center">
      <h1>Azərbaycan Əmək və <br>Sosial Münasibətlər<br>Akademiyası</h1>
      <img src="https://www.ahik.org/storage/pages/1/whatsapp-image-2025-08-26-at-180001-1.jpg" alt="foto" />
      <div class="text-and-degrees">
        <p>
          Azərbaycan Əmək və Sosial Münasibətlər Akademiyası <br>2006‑cı ildə yaradılmışdır və müstəqil ali təhsil müəssisəsi kimi fəaliyyət göstərir.<br>
          Bu gün AƏSMA müasir əmək bazarının tələblərinə uyğun yüksəkixtisaslı <br>kadrların hazırlanmasını həyata keçirir.Həmçinin akademiyada son illerde <br>
          tələbələrin ixtisaslaşmış kadr kimi formalaşması <br>məqsədilə müxtəlif təlim kursları, könüllülük layihələri və digər innovativ <br>
          təşəbbüslər həyata keçirilərək onların peşəkar bacarıqları və<br> sosial aktivliyi artırılır.<br>
          Akademiyada iki fakültə – “Maliyyə-İqtisad” və “Sosial iş” fakültələri fəaliyyət göstərir.<br>
          Akademiyada bir kitabxana, iki akt zalı və bir inkişaf mərkəzi mövcuddur. Hər bir xüsusi gün xüsusi diqqət mərkəzində saxlanılaraq, həmin günlərin əhəmiyyətinə uyğun tədbirlər sistemli şəkildə təşkil olunur.
        </p>
        <div class="degree-section">
          <div class="degree-box">
            <h2>Bakalavriat səviyyəsində ixtisaslar:</h2>
            <ul>
              <li>Sosial iş</li>
              <li>Marketinq</li>
              <li>Dövlət və bələdiyyə idarəetməsi</li>
              <li>Maliyyə</li>
              <li>Mühasibat</li>
              <li>İqtisadiyyat</li>
            </ul>
            <div class="small-bg"></div>
          </div>
          <div class="degree-box">
            <h2>Magistratura səviyyəsində ixtisaslar:</h2>
            <ul>
              <li>Maliyyə</li>
              <li>Mühasibat uçotu və audit</li>
              <li>İqtisadiyyat</li>
              <li>Marketinq</li>
              <li>Sosial iş</li>
            </ul>
            <div class="small-bg"></div>
          </div>
        </div>
      </div>
      <h2>Böyük Akt Zalı</h2>
      <div class="act-hall-section">
        <img src="https://api.aesma.edu.az/dist/images/posts/0cfad814-bc6d-4372-8a30-b88a56080fa1.jpg" alt="Böyük Akt Zalı Şəkli" />
        <p>
          Azərbaycanda Teatr Memarlığı- XIX əsrin birinci yarısının sonlarında tamaşa binaları artıq Azərbaycan şəhərlərinin srukturuna daxil idi.
          Peşəkar teatr deyəndə və onun fəaliyyəti barədə düşünəndə sözsüz ki, ilk növbədə sənət ocağının yerləşdiyi bina barədə fikirlər oyanır.
          Elm sübut edib ki, teatr tamaşasının təlqin etdiyi bədii-estetik zövqün kökündə tamaşa oynanılan binanın texniki imkanları və texnologiyası da mühüm yer tutur.
          Teatr binasının arxitektura özəllikləri müxtəlif şəkillərdə səhnə sənətinin gözəllik estetikasını istiqamətləndirir, onun özünəməxsusluğunun bədii səciyyələrini müəyyənləşdirir.
        </p>
      </div>
      <h2>Kiçik Akt Zalı</h2>
      <div class="act-hall-section reverse">
        <p>
          Ekoloji tərbiyə ətraf mühitin dərk olunması və təbiətə qayğı ilə yanaşmanın formalaşması proseslərindən keçir.
          Ekoloji cəhətdən savadlı insan dərk etməlidir ki, təbiət də onun özü kimi canlıdır.
          Təbiət güclüdür, ancaq bu güc tükənməz deyil.
          Təhsil ocaqlarında ekoloji təhsilin gücləndirilməsinin tərəfdarları hesab edirlər ki,
          uşağa kiçik yaşlarından təbiətə qayğı ilə yanaşmanı aşılamaqla biz onun şəxsiyyətinin formalaşmasına ciddi təkan vermiş oluruq.
          Başqa sözlə, yeni nəsildə vətəndaş şüurunun formalaşdırılmasının əsas istiqamətlərindən biri də məhz ekoloji təhsil və tərbiyə olmalıdır.
          Bu yolla gəncləri doğma torpağı və təbiəti sevməyə, ətraf mühitə biganəlikdən qaçmağa öyrədə bilərik.
        </p>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsxxCDkjDQApaNQm--r8Pd_b3GZvRr3P29E0OfN2aHKJaZprShsxT9x-Md2491qb510YA&usqp=CAU" alt="Kiçik Akt Zalı Şəkli" />
      </div>
      <div class="footer-hours">
        <h3>Akademiyanın iş saatları</h3>
        <img src="https://cdn-icons-png.flaticon.com/512/747/747310.png" alt="Saat ikonu" class="clock-icon" />
        <ul>
          <li><strong>Bazar ertəsi - Cümə:</strong> 09:00 – 18:00</li>
          <li><strong>Şənbə-Bazar:</strong> Bağlıdır</li>
        </ul>
      </div>
    </div>
  </div>
</body>
</html>
    """)
if __name__ == "__main__":
    app.run(debug=True)                