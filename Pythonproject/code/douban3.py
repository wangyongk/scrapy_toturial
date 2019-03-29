#coding=utf-8
import requests
#from lxml import etree
from lxml import html
etree = html.etree

htmldoc="""<!DOCTYPE html><html lang="zh-cmn-Hans" class="ua-windows ua-webkit"><head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">
    <meta name="referrer" content="always">
    <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
    <title>
        肖申克的救赎 (豆瓣)
</title>

    <meta name="baidu-site-verification" content="cZdR4xxR7RxmM4zE" />
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">

    <link rel="apple-touch-icon" href="https://img3.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png">
    <link href="https://img3.doubanio.com/f/shire/bf61b1fa02f564a4a8f809da7c7179b883a56146/css/douban.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/shire/ae3f5a3e3085968370b1fc63afcecb22d3284848/css/separation/_all.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/movie/8864d3756094f5272d3c93e30ee2e324665855b0/css/movie/base/init.css" rel="stylesheet">
    <script type="text/javascript">var _head_start = new Date();</script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/movie/0495cb173e298c28593766009c7b0a953246c5b5/js/movie/lib/jquery.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/f783ad4a9e451cfd44ee9c3f6f986706169525a7/js/douban.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/0efdc63b77f895eaf85281fb0e44d435c6239a3f/js/separation/_all.js"></script>

    <meta name="keywords" content="肖申克的救赎,The Shawshank Redemption,肖申克的救赎影评,剧情介绍,电影图片,预告片,影讯,在线购票,论坛,肖申克的救赎在线观看,肖申克的救赎高清,肖申克的救赎在线播放">
    <meta name="description" content="肖申克的救赎电影简介和剧情介绍,肖申克的救赎影评、图片、预告片、影讯、论坛、在线购票、肖申克的救赎在线观看、高清、在线播放">
    <meta name="mobile-agent" content="format=html5; url=http://m.douban.com/movie/subject/1292052/"/>
    <link rel="alternate" href="android-app://com.douban.movie/doubanmovie/subject/1292052/" />
    <link rel="stylesheet" href="https://img3.doubanio.com/dae/cdnlib/libs/LikeButton/1.0.5/style.min.css">
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>
    <script type="text/javascript">
      Do.add('dialog', {path: 'https://img3.doubanio.com/f/shire/4ea3216519a6183c7bcd4f7d1a6d4fd57ce1a244/js/ui/dialog.js', type: 'js'});
      Do.add('dialog-css', {path: 'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css', type: 'css'});
      Do.add('handlebarsjs', {path: 'https://img3.doubanio.com/f/movie/3d4f8e4a8918718256450eb6e57ec8e1f7a2e14b/js/movie/lib/handlebars.current.js', type: 'js'});
    </script>

  <script type='text/javascript'>
  var _vwo_code = (function() {
    var account_id = 249272,
      settings_tolerance = 0,
      library_tolerance = 2500,
      use_existing_jquery = false,
      // DO NOT EDIT BELOW THIS LINE
      f=false,d=document;return{use_existing_jquery:function(){return use_existing_jquery;},library_tolerance:function(){return library_tolerance;},finish:function(){if(!f){f=true;var a=d.getElementById('_vis_opt_path_hides');if(a)a.parentNode.removeChild(a);}},finished:function(){return f;},load:function(a){var b=d.createElement('script');b.src=a;b.type='text/javascript';b.innerText;b.onerror=function(){_vwo_code.finish();};d.getElementsByTagName('head')[0].appendChild(b);},init:function(){settings_timer=setTimeout('_vwo_code.finish()',settings_tolerance);var a=d.createElement('style'),b='body{opacity:0 !important;filter:alpha(opacity=0) !important;background:none !important;}',h=d.getElementsByTagName('head')[0];a.setAttribute('id','_vis_opt_path_hides');a.setAttribute('type','text/css');if(a.styleSheet)a.styleSheet.cssText=b;else a.appendChild(d.createTextNode(b));h.appendChild(a);this.load('//dev.visualwebsiteoptimizer.com/j.php?a='+account_id+'&u='+encodeURIComponent(d.URL)+'&r='+Math.random());return settings_timer;}};}());

  +function () {
    var bindEvent = function (el, type, handler) {
        var $ = window.jQuery || window.Zepto || window.$
       if ($ && $.fn && $.fn.on) {
           $(el).on(type, handler)
       } else if($ && $.fn && $.fn.bind) {
           $(el).bind(type, handler)
       } else if (el.addEventListener){
         el.addEventListener(type, handler, false);
       } else if (el.attachEvent){
         el.attachEvent("on" + type, handler);
       } else {
         el["on" + type] = handler;
       }
     }

    var _origin_load = _vwo_code.load
    _vwo_code.load = function () {
      var args = [].slice.call(arguments)
      bindEvent(window, 'load', function () {
        _origin_load.apply(_vwo_code, args)
      })
    }
  }()

  _vwo_settings_timer = _vwo_code.init();
  </script>





<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "name": "肖申克的救赎 The Shawshank Redemption",
  "url": "/subject/1292052/",
  "image": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp",
  "director":
  [
    {
      "@type": "Person",
      "url": "/celebrity/1047973/",
      "name": "弗兰克·德拉邦特 Frank Darabont"
    }
  ]
,
  "author":
  [
    {
      "@type": "Person",
      "url": "/celebrity/1047973/",
      "name": "弗兰克·德拉邦特 Frank Darabont"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1049547/",
      "name": "斯蒂芬·金 Stephen King"
    }
  ]
,
  "actor":
  [
    {
      "@type": "Person",
      "url": "/celebrity/1054521/",
      "name": "蒂姆·罗宾斯 Tim Robbins"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1054534/",
      "name": "摩根·弗里曼 Morgan Freeman"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1041179/",
      "name": "鲍勃·冈顿 Bob Gunton"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1000095/",
      "name": "威廉姆·赛德勒 William Sadler"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1013817/",
      "name": "克兰西·布朗 Clancy Brown"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1010612/",
      "name": "吉尔·贝罗斯 Gil Bellows"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1054892/",
      "name": "马克·罗斯顿 Mark Rolston"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1027897/",
      "name": "詹姆斯·惠特摩 James Whitmore"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1087302/",
      "name": "杰弗里·德曼 Jeffrey DeMunn"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1074035/",
      "name": "拉里·布兰登伯格 Larry Brandenburg"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1099030/",
      "name": "尼尔·吉恩托利 Neil Giuntoli"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1343305/",
      "name": "布赖恩·利比 Brian Libby"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1048222/",
      "name": "大卫·普罗瓦尔 David Proval"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1343306/",
      "name": "约瑟夫·劳格诺 Joseph Ragno"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1315528/",
      "name": "祖德·塞克利拉 Jude Ciccolella"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1014040/",
      "name": "保罗·麦克兰尼 Paul McCrane"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1390795/",
      "name": "芮妮·布莱恩 Renee Blaine"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1083603/",
      "name": "阿方索·弗里曼 Alfonso Freeman"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1330490/",
      "name": "V·J·福斯特 V.J. Foster"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1000635/",
      "name": "弗兰克·梅德拉诺 Frank Medrano"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1390797/",
      "name": "马克·迈尔斯 Mack Miles"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1150160/",
      "name": "尼尔·萨默斯 Neil Summers"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1048233/",
      "name": "耐德·巴拉米 Ned Bellamy"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1000721/",
      "name": "布赖恩·戴拉特 Brian Delate"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1333685/",
      "name": "唐·麦克马纳斯 Don McManus"
    }
  ]
,
  "datePublished": "1994-09-10",
  "genre": ["\u72af\u7f6a", "\u5267\u60c5"],
  "duration": "PT2H22M",
  "description": "20世纪40年代末，小有成就的青年银行家安迪（蒂姆·罗宾斯 Tim Robbins 饰）因涉嫌杀害妻子及她的情人而锒铛入狱。在这座名为肖申克的监狱内，希望似乎虚无缥缈，终身监禁的惩罚无疑注定了安迪接下...",
  "@type": "Movie",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingCount": "1284188",
    "bestRating": "10",
    "worstRating": "2",
    "ratingValue": "9.6"
  }
}
</script>


    <style type="text/css">

</style>
    <style type="text/css">img { max-width: 100%; }</style>
    <script type="text/javascript"></script>
    <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/2e095ab269d6515b.css">

    <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
</head>

<body>

    <script type="text/javascript">var _body_start = new Date();</script>






    <link href="//img3.doubanio.com/dae/accounts/resources/984c231/shire/bundle.css" rel="stylesheet" type="text/css">



<div id="db-global-nav" class="global-nav">
  <div class="bd">

<div class="top-nav-info">
  <ul>
    <li>
    <a id="top-nav-doumail-link" href="https://www.douban.com/doumail/">豆邮</a>
    </li>
    <li class="nav-user-account">
      <a target="_blank" href="https://accounts.douban.com/passport/setting/" class="bn-more">
        <span>永康的帐号</span><span class="arrow"></span>
      </a>
      <div class="more-items">
        <table cellpadding="0" cellspacing="0">
          <tbody>
            <tr>
              <td>
                <a href="https://www.douban.com/mine/">个人主页</a>
              </td>
            </tr>
            <tr>
              <td>
                <a target="_blank" href="https://www.douban.com/mine/orders/">我的订单</a>
              </td>
            </tr>
            <tr>
              <td>
                <a target="_blank" href="https://www.douban.com/mine/wallet/">我的钱包</a>
              </td>
            </tr>
            <tr>
              <td>
                <a target="_blank" href="https://accounts.douban.com/passport/setting/">帐号管理</a>
              </td>
            </tr>
            <tr>
              <td>
                <a href="https://www.douban.com/accounts/logout?source=movie&ck=to2S">退出</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
  </ul>
</div>

  <div class="top-nav-reminder">
    <a href="https://www.douban.com/notification/" class="lnk-remind">提醒</a>
    <div id="top-nav-notimenu" class="more-items">
      <div class="bd">
        <p>加载中...</p>
      </div>
    </div>
  </div>

    <div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="doubanapp-tip">
    <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
    <a href="javascript: void 0;" class="tip-close">×</a>
  </div>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
  </div>
</div>




<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;181757233&quot;}">豆瓣</a>
    </li>
    <li class="">
      <a href="https://book.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;181757233&quot;}">读书</a>
    </li>
    <li class="on">
      <a href="https://movie.douban.com"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;181757233&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;181757233&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;181757233&quot;}">同城</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;181757233&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;181757233&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;181757233&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://time.douban.com&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;181757233&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;181757233&quot;}">豆品</a>
    </li>
    <li>
      <a href="#more" class="bn-more"><span>更多</span></a>
      <div class="more-items">
        <table cellpadding="0" cellspacing="0">
          <tbody>
            <tr>
              <td>
                <a href="https://ypy.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-ypy&quot;,&quot;uid&quot;:&quot;181757233&quot;}">豆瓣摄影</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    USER_ID: "181757233",
    UPLOAD_AUTH_TOKEN: "181757233:5e40726c13efc9a4389f6b5169f6d7aad888be0f",
    SSE_TOKEN: "257375ddc870fec69eccfe207edfd10f71efe957",
    SSE_TIMESTAMP: "1548592939",
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script>



    <script src="//img3.doubanio.com/dae/accounts/resources/984c231/shire/bundle.js" defer="defer"></script>








    <link href="//img3.doubanio.com/dae/accounts/resources/8c80301/movie/bundle.css" rel="stylesheet" type="text/css">




<div id="db-nav-movie" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="https:&#47;&#47;movie.douban.com">豆瓣电影</a>
    </div>
    <div class="nav-search">
      <form action="https:&#47;&#47;movie.douban.com/subject_search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="搜索电影、电视剧、综艺、影人" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1002" />
        </fieldset>
      </form>
    </div>
  </div>
  </div>
  <div class="nav-secondary">


<div class="nav-items">
  <ul>
    <li    ><a href="https://movie.douban.com/mine"
     >我看</a>
    </li>
    <li    ><a href="https://movie.douban.com/cinema/nowplaying/"
     >影讯&购票</a>
    </li>
    <li    ><a href="https://movie.douban.com/explore"
     >选电影</a>
    </li>
    <li    ><a href="https://movie.douban.com/tv/"
     >电视剧</a>
    </li>
    <li    ><a href="https://movie.douban.com/chart"
     >排行榜</a>
    </li>
    <li    ><a href="https://movie.douban.com/tag/"
     >分类</a>
    </li>
    <li    ><a href="https://movie.douban.com/review/best/"
     >影评</a>
    </li>
    <li    ><a href="https://movie.douban.com/annual/2018?source=navigation"
     >2018年度榜单</a>
    </li>
    <li    ><a href="https://www.douban.com/standbyme/2018?source=navigation"
     >2018书影音报告</a>
    </li>
  </ul>
</div>

    <a href="https://movie.douban.com/annual/2018?source=movie_navigation" class="movieannual2018"></a>
  </div>
</div>

<script id="suggResult" type="text/x-jquery-tmpl">
  <li data-link="{{= url}}">
            <a href="{{= url}}" onclick="moreurl(this, {from:'movie_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
            <img src="{{= img}}" width="40" />
            <p>
                <em>{{= title}}</em>
                {{if year}}
                    <span>{{= year}}</span>
                {{/if}}
                {{if sub_title}}
                    <br /><span>{{= sub_title}}</span>
                {{/if}}
                {{if address}}
                    <br /><span>{{= address}}</span>
                {{/if}}
                {{if episode}}
                    {{if episode=="unknow"}}
                        <br /><span>集数未知</span>
                    {{else}}
                        <br /><span>共{{= episode}}集</span>
                    {{/if}}
                {{/if}}
            </p>
        </a>
        </li>
  </script>




    <script src="//img3.doubanio.com/dae/accounts/resources/8c80301/movie/bundle.js" defer="defer"></script>






    <div id="wrapper">



    <div id="content">

    <!-- top 250 begin -->

    <div class="top250"><span class="top250-no">No.1</span><span class="top250-link"><a href="https://movie.douban.com/top250" target="_blank">豆瓣电影Top250</a></span>
    </div>

    <!-- top 250 end -->

    <div id="dale_movie_subject_top_icon"></div>
    <h1>
        <span property="v:itemreviewed">肖申克的救赎 The Shawshank Redemption</span>
            <span class="year">(1994)</span>
    </h1>

        <div class="grid-16-8 clearfix">



            <div class="article">









        <div class="indent clearfix">
            <div class="subjectwrap clearfix">
                <div class="subject clearfix">




<div id="mainpic" class="">
    <a class="nbgnbg" href="https://movie.douban.com/subject/1292052/photos?type=R" title="点击看更多海报">
        <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp" title="点击看更多海报" alt="The Shawshank Redemption" rel="v:image" />
   </a>
                <p class="gact"><a href="https://movie.douban.com/subject/1292052/edit">更新描述或海报</a></p>
</div>




<div id="info">
        <span ><span class='pl'>导演</span>: <span class='attrs'><a href="/celebrity/1047973/" rel="v:directedBy">弗兰克·德拉邦特</a></span></span><br/>
        <span ><span class='pl'>编剧</span>: <span class='attrs'><a href="/celebrity/1047973/">弗兰克·德拉邦特</a> / <a href="/celebrity/1049547/">斯蒂芬·金</a></span></span><br/>
        <span class="actor"><span class='pl'>主演</span>: <span class='attrs'><a href="/celebrity/1054521/" rel="v:starring">蒂姆·罗宾斯</a> / <a href="/celebrity/1054534/" rel="v:starring">摩根·弗里曼</a> / <a href="/celebrity/1041179/" rel="v:starring">鲍勃·冈顿</a> / <a href="/celebrity/1000095/" rel="v:starring">威廉姆·赛德勒</a> / <a href="/celebrity/1013817/" rel="v:starring">克兰西·布朗</a> / <a href="/celebrity/1010612/" rel="v:starring">吉尔·贝罗斯</a> / <a href="/celebrity/1054892/" rel="v:starring">马克·罗斯顿</a> / <a href="/celebrity/1027897/" rel="v:starring">詹姆斯·惠特摩</a> / <a href="/celebrity/1087302/" rel="v:starring">杰弗里·德曼</a> / <a href="/celebrity/1074035/" rel="v:starring">拉里·布兰登伯格</a> / <a href="/celebrity/1099030/" rel="v:starring">尼尔·吉恩托利</a> / <a href="/celebrity/1343305/" rel="v:starring">布赖恩·利比</a> / <a href="/celebrity/1048222/" rel="v:starring">大卫·普罗瓦尔</a> / <a href="/celebrity/1343306/" rel="v:starring">约瑟夫·劳格诺</a> / <a href="/celebrity/1315528/" rel="v:starring">祖德·塞克利拉</a> / <a href="/celebrity/1014040/" rel="v:starring">保罗·麦克兰尼</a> / <a href="/celebrity/1390795/" rel="v:starring">芮妮·布莱恩</a> / <a href="/celebrity/1083603/" rel="v:starring">阿方索·弗里曼</a> / <a href="/celebrity/1330490/" rel="v:starring">V·J·福斯特</a> / <a href="/celebrity/1000635/" rel="v:starring">弗兰克·梅德拉诺</a> / <a href="/celebrity/1390797/" rel="v:starring">马克·迈尔斯</a> / <a href="/celebrity/1150160/" rel="v:starring">尼尔·萨默斯</a> / <a href="/celebrity/1048233/" rel="v:starring">耐德·巴拉米</a> / <a href="/celebrity/1000721/" rel="v:starring">布赖恩·戴拉特</a> / <a href="/celebrity/1333685/" rel="v:starring">唐·麦克马纳斯</a></span></span><br/>
        <span class="pl">类型:</span> <span property="v:genre">剧情</span> / <span property="v:genre">犯罪</span><br/>

        <span class="pl">制片国家/地区:</span> 美国<br/>
        <span class="pl">语言:</span> 英语<br/>
        <span class="pl">上映日期:</span> <span property="v:initialReleaseDate" content="1994-09-10(多伦多电影节)">1994-09-10(多伦多电影节)</span> / <span property="v:initialReleaseDate" content="1994-10-14(美国)">1994-10-14(美国)</span><br/>
        <span class="pl">片长:</span> <span property="v:runtime" content="142">142分钟</span><br/>
        <span class="pl">又名:</span> 月黑高飞(港) / 刺激1995(台) / 地狱诺言 / 铁窗岁月 / 消香克的救赎<br/>
        <span class="pl">IMDb链接:</span> <a href="http://www.imdb.com/title/tt0111161" target="_blank" rel="nofollow">tt0111161</a><br>

</div>




                </div>



<div id="interest_sectl">
    <div class="rating_wrap clearbox" rel="v:rating">
        <div class="clearfix">
          <div class="rating_logo ll">豆瓣评分</div>
          <div class="output-btn-wrap rr" style="display:none">
            <img src="https://img3.doubanio.com/f/movie/692e86756648f29457847c5cc5e161d6f6b8aaac/pics/movie/reference.png" />
            <a class="download-output-image" href="#">引用</a>
          </div>


        </div>



<div class="rating_self clearfix" typeof="v:Rating">
    <strong class="ll rating_num" property="v:average">9.6</strong>
    <span property="v:best" content="10.0"></span>
    <div class="rating_right ">
        <div class="ll bigstar bigstar50"></div>
        <div class="rating_sum">
                <a href="collections" class="rating_people"><span property="v:votes">1284269</span>人评价</a>
        </div>
    </div>
</div>
<div class="ratings-on-weight">

        <div class="item">

        <span class="stars5 starstop" title="力荐">
            5星
        </span>
        <div class="power" style="width:64px"></div>
        <span class="rating_per">83.9%</span>
        <br />
        </div>
        <div class="item">

        <span class="stars4 starstop" title="推荐">
            4星
        </span>
        <div class="power" style="width:10px"></div>
        <span class="rating_per">14.3%</span>
        <br />
        </div>
        <div class="item">

        <span class="stars3 starstop" title="还行">
            3星
        </span>
        <div class="power" style="width:1px"></div>
        <span class="rating_per">1.6%</span>
        <br />
        </div>
        <div class="item">

        <span class="stars2 starstop" title="较差">
            2星
        </span>
        <div class="power" style="width:0px"></div>
        <span class="rating_per">0.1%</span>
        <br />
        </div>
        <div class="item">

        <span class="stars1 starstop" title="很差">
            1星
        </span>
        <div class="power" style="width:0px"></div>
        <span class="rating_per">0.1%</span>
        <br />
        </div>
</div>

    </div>

        <div class="rating_betterthan">
            好于 <a href="/typerank?type_name=剧情&type=11&interval_id=100:90&action=">99% 剧情片</a><br/>
            好于 <a href="/typerank?type_name=犯罪&type=3&interval_id=100:90&action=">99% 犯罪片</a><br/>
        </div>
</div>



            </div>





<div id="interest_sect_level" class="clearfix">

            <a href="https://movie.douban.com/subject/1292052/?interest=wish&amp;ck=to2S" rel="nofollow" class="collect_btn colbutt ll" name="pbtn-1292052-wish">
                <span>想看</span>
            </a>
            <a href="https://movie.douban.com/subject/1292052/?interest=collect&amp;ck=to2S" rel="nofollow" class="collect_btn colbutt ll" name="pbtn-1292052-collect">
                <span>看过</span>
            </a>
        <div class="ll j a_stars">


    评价:
    <span id="rating"> <span id="stars" data-solid="https://img3.doubanio.com/f/shire/5a2327c04c0c231bced131ddf3f4467eb80c1c86/pics/rating_icons/star_onmouseover.png" data-hollow="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" data-solid-2x="https://img3.doubanio.com/f/shire/7258904022439076d57303c3b06ad195bf1dc41a/pics/rating_icons/star_onmouseover@2x.png" data-hollow-2x="https://img3.doubanio.com/f/shire/95cc2fa733221bb8edd28ad56a7145a5ad33383e/pics/rating_icons/star_hollow_hover@2x.png">

                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-1292052-collect-1">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star1" width="16" height="16"/></a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-1292052-collect-2">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star2" width="16" height="16"/></a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-1292052-collect-3">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star3" width="16" height="16"/></a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-1292052-collect-4">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star4" width="16" height="16"/></a>
                    <a href="javascript:;" class="j a_collect_btn" name="pbtn-1292052-collect-5">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star5" width="16" height="16"/></a>
    </span><span id="rateword" class="pl"></span>
    <input id="n_rating" type="hidden" value=""  />
    </span>

        </div>


</div>





















<div class="gtleft">
    <ul class="ul_subject_menu bicelink color_gray pt6 clearfix">



                <li>
    <img src="https://img3.doubanio.com/f/shire/cc03d0fcf32b7ce3af7b160a0b85e5e66b47cc42/pics/short-comment.gif" />&nbsp;
        <a onclick="moreurl(this, {from:'mv_sbj_wr_cmnt'})" href="javascript:;" class="j a_collect_btn" name="cbtn-1292052">写短评</a>
 </li>
                    <li>

    <img src="https://img3.doubanio.com/f/shire/5bbf02b7b5ec12b23e214a580b6f9e481108488c/pics/add-review.gif" />&nbsp;
        <a onclick="moreurl(this, {from:'mv_sbj_wr_rv'})" class="create_from_menu" href="https://movie.douban.com/subject/1292052/new_review" rel="nofollow">写影评</a>
 </li>
                    <li>
    <img src="https://img3.doubanio.com/f/shire/61cc48ba7c40e0272d46bb93fe0dc514f3b71ec5/pics/add-doulist.gif" />&nbsp;
    <a href="/subject/1292052/questions/ask?from=subject_top">提问题</a>
 </li>
                <li>



    <div class="doulist-add-btn">





  <a href="javascript:void(0)"
     data-id="1292052"
     data-cate="1002"
     data-canview="True"
     data-url="https://movie.douban.com/subject/1292052/"
     data-catename="电影"
     data-link="https://www.douban.com/people/181757233/doulists/all?add=1292052&amp;cat=1002"
     data-title="肖申克的救赎 The Shawshank Redemption"
     data-picture="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp"
     class="lnk-doulist-add"
     onclick="moreurl(this, { 'from':'doulist-btn-1002-1292052-181757233'})">
      <i></i>添加到豆列
  </a>
    </div>

 </li>
                <li>




    <span class="rec" id="电影-1292052">
    <a href= "#"
        data-type="电影"
        data-url="https://movie.douban.com/subject/1292052/"
        data-desc="电影《肖申克的救赎 The Shawshank Redemption》 (来自豆瓣) "
        data-title="电影《肖申克的救赎 The Shawshank Redemption》 (来自豆瓣) "
        data-pic="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpeg"
        class="bn-sharing ">
        分享到
    </a> &nbsp;&nbsp;
    </span>

    <script>
        if (!window.DoubanShareMenuList) {
            window.DoubanShareMenuList = [];
        }
        var __cache_url = __cache_url || {};

        (function(u){
            if(__cache_url[u]) return;
            __cache_url[u] = true;
            window.DoubanShareIcons = 'https://img3.doubanio.com/f/shire/d15ffd71f3f10a7210448fec5a68eaec66e7f7d0/pics/ic_shares.png';

            var initShareButton = function() {
                $.ajax({url:u,dataType:'script',cache:true});
            };

            if (typeof Do == 'function' && 'ready' in Do) {
                Do(
                    'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css',
                    'https://img3.doubanio.com/f/shire/4ea3216519a6183c7bcd4f7d1a6d4fd57ce1a244/js/ui/dialog.js',
                    'https://img3.doubanio.com/f/movie/c4ab132ff4d3d64a83854c875ea79b8b541faf12/js/movie/lib/qrcode.min.js',
                    initShareButton
                );
            } else if(typeof Douban == 'object' && 'loader' in Douban) {
                Douban.loader.batch(
                    'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css',
                    'https://img3.doubanio.com/f/shire/4ea3216519a6183c7bcd4f7d1a6d4fd57ce1a244/js/ui/dialog.js',
                    'https://img3.doubanio.com/f/movie/c4ab132ff4d3d64a83854c875ea79b8b541faf12/js/movie/lib/qrcode.min.js'
                ).done(initShareButton);
            }

        })('https://img3.doubanio.com/f/movie/32be6727ed3ad8f6c4a417d8a086355c3e7d1d27/js/movie/lib/sharebutton.js');
    </script>


  </li>


    </ul>

    <script type="text/javascript">
        $(function(){
            $(".ul_subject_menu li.rec .bn-sharing").bind("click", function(){
                $.get("/blank?sbj_page_click=bn_sharing");
            });
            $(".ul_subject_menu .create_from_menu").bind("click", function(e){
                e.preventDefault();
                var $el = $(this);
                var glRoot = document.getElementById('gallery-topics-selection');
                if (window.has_gallery_topics && glRoot) {
                    // 判断是否有话题
                    glRoot.style.display = 'block';
                } else {
                    location.href = $el.attr('href');
                }
            });
        });
    </script>
</div>









        <style type="text/css">

.suggestions-list li { position: relative; left: 0; top: 0; margin-bottom: 7px; height: 35px }
.suggestions-list li .user-thumb { display: inline-block; *display: inline; float: left; margin: 2px 5px 0 0; vertical-align: top }
.suggestions-list li .user-thumb img { width: 25px; height: 25px }
.suggestions-list li .user-name-info { display: inline-block; *display: inline; line-height: 1.4em }
.suggestions-list li .user-name-info .user-profile-link { color: #333; font-weight: 800 }
.suggestions-list li .user-name-info .user-profile-link:hover { color: #4b8dc5 }
.suggestions-list li .user-name-info p { color: #999 }
.suggestions-list li .user-name-info b { color: #4b8dc5; font-weight: normal; cursor: pointer }
.suggestions-list li .user-name-info b:hover { text-decoration: underline }
.suggestions-list li .dismiss { position: absolute }
.suggestions-list li .dismiss { color: #aaa; margin: 0 0 0 10px; top: 0; right: 0 }
.suggestions-list li .dismiss:hover { color: #333; text-decoration: none }


.suggest-overlay { position: absolute; z-index: 99; width: auto; background: #fff; border: 1px solid #c5c7d2;
    -moz-border-radius : 3px;
    -webkit-border-radius : 3px;
    border-radius: 3px
}
.suggest-overlay .bd { min-width: 220px; line-height: 1; background: #fafafa; color: #b3b3b3; padding: 5px;
    -moz-border-radius : 3px;
    -webkit-border-radius : 3px;
    border-radius: 3px
}
.suggest-overlay ul { color: #999; padding: 3px 0; min-width: 214px }
.suggest-overlay li { cursor: pointer; padding: 3px 7px }
.suggest-overlay li b { font-weight: bold }
.suggest-overlay li .username { color: #333 }
.suggest-overlay img { margin-right: 5px; width: 20px; height: 20px; vertical-align: middle }
.suggest-overlay .on { background: #e9f0f8 }

.mentioned-highlighter { font: 14px/20px "Helvetica Neue",Helvetica,Arial,sans-serif; position: absolute; left: 4px; top: 4px; font-size: 14px; height: 60px; width: 98.5%; overflow: hidden; background: #fff; white-space: pre-wrap; word-wrap: break-word; color: transparent }
.mentioned-highlighter b { font-weight: normal; background-color: #d2e1f3; color: transparent;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
  border-radius: 2px
}

            .movie-share-dialog .bn-flat input {
    font-size: 14px;
}
.movie-share-dialog {
    z-index: 100;
}
.movie-share-dialog .form-ft-inner{
    text-align: right;
}
.movie-share-dialog div.bd {
    padding: 0;
}

.movie-share .form-bd .input-area {
    position: relative;
    margin: 15px;
    height: 91px;
    zoom: 1;
}

.movie-share-no-media .form-bd {
    height: 140px;
}

.movie-share-dialog .share-text {
    height: 85px;
    position: absolute;
    z-index: 9;
    background: transparent;
    font: 14px/18px "Helvetica Neue",Helvetica,Arial,sans-serif;
    width: 98%;
    -webkit-border-radius: 4px 4px 4px 4px;
    border-radius: 4px 4px 4px 4px;
}

.movie-share-dialog .mentioned-highlighter {
    width: 483px;
    padding: 3px 4px 4px;
    color: white;
    position: absolute;
    top:0;
    left:0;
    z-index: 0;
}

.movie-share-dialog .mentioned-highlighter code {
    color: #D2E1F3;
    background: #D2E1F3;
    border-radius: 2px;
    padding-right: 1px;
    display: inline-block;
    font: 14px/18px "Helvetica Neue",Helvetica,Arial,sans-serif;
}


.movie-share .form-ft {
    background: #e9eef2;
    height: 25px;
    padding-top: 10px;
    padding-bottom: 10px;
}

.movie-share .form-ft-inner {
    height: 25px;
    padding-left: 15px;
    padding-right: 15px;
}

.movie-share-dialog .dialog-only-text {
    text-align: center;
    font-size: 14px;
    line-height: 1.5;
    padding-top: 30px;
    padding-bottom: 30px;
    color: #0c7823;
}

.movie-share-dialog .ll {
    float: left;
    display: inline;
}
.movie-share-dialog .share-label {
    width: auto;
    display: inline;
    float: none;
}

.movie-share-dialog .leading-label {
    _vertical-align: -2px;
}
.movie-share-dialog .media {
    float: left;
    margin-right: 10px;
    max-width: 100px;
    max-height: 100px;
    *width: 100px;
}
.movie-share-dialog .info-area{
    overflow: hidden;
    zoom: 1;
    margin: 0 15px 15px;
    height: 100px;
}
.movie-share-dialog .info-area strong{
    font-weight: bold;
}
.movie-share-dialog .info-area p{
    margin: 3px 0;
    color: #999;
}

.movie-share-dialog #sync-setting {
    _vertical-align: -5px;
    margin-left: 10px;
}

.movie-share-dialog .info-area .server-error {
    position: absolute;
    bottom: 45px;
    right: 15px;
    color: red;
}

.movie-share-dialog .avail-num-indicator {
    color: #aaa;
    font-weight: 800;
    padding-right: 3px;
}

.movie-share-dialog .bottom-setting {
    width: 432px;
}
.movie-share-dialog .input-checkbox {
    vertical-align: -2px;
    _vertical-align: -1px;
}

.movie-share-dialog #sync-setting img {
    _vertical-align: 2px;
}



.suggest-overlay {
    z-index: 2000;
}

.movie-bar {
    position: relative;
    margin-top: 10px;
}

.movie-bar-fav {
    position: absolute;
    top: 0;
    right: 0;
}

        </style>
        <script src="https://img3.doubanio.com/f/shire/a40c5220b3f40ce737b366c0030ecf810b37bfea/js/lib/mustache.js" type="text/javascript"></script>
        <script src="https://img3.doubanio.com/f/shire/1d985568f3cc434b145983919d9954e2ca627e9c/js/lib/textarea-mention.js" type="text/javascript"></script>
        <script src="https://img3.doubanio.com/f/movie/6b10694c6523e81ebdea9963901b757cf91387f6/js/movie/share.js" type="text/javascript"></script>

<div class="rec-sec">
<span class="rec">
    <script id="movie-share" type="text/x-html-snippet">

    <form class="movie-share" action="/j/share" method="POST"><div style="display:none;"><input type="hidden" name="ck" value="to2S"/></div>
        <div class="clearfix form-bd">
            <div class="input-area">
                <textarea name="text" class="share-text" cols="72" data-mention-api="https://api.douban.com/shuo/in/complete?alt=xd&amp;callback=?"></textarea>
                <input type="hidden" name="target-id" value="1292052">
                <input type="hidden" name="target-type" value="0">
                <input type="hidden" name="title" value="肖申克的救赎 The Shawshank Redemption‎ (1994)">
                <input type="hidden" name="desc" value="导演 弗兰克·德拉邦特 主演 蒂姆·罗宾斯 / 摩根·弗里曼 / 美国 / 9.6分(1284269评价)">
                <input type="hidden" name="redir" value=""/>
                <div class="mentioned-highlighter"></div>
            </div>

            <div class="info-area">
                    <img class="media" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp" />
                <strong>肖申克的救赎 The Shawshank Redemption‎ (1994)</strong>
                <p>导演 弗兰克·德拉邦特 主演 蒂姆·罗宾斯 / 摩根·弗里曼 / 美国 / 9.6分(1284269评价)</p>
                <p class="error server-error">&nbsp;</p>
            </div>
        </div>
        <div class="form-ft">
            <div class="form-ft-inner">





<div class="sync-setting pl">
    <label>分享到</label>



            <a id="lnk-sync-setting" class="no-visited no-hover" href="https://movie.douban.com/settings/sync" target="_blank"
                class="pl share-label"><img src="https://img3.doubanio.com/f/movie/9389c4e5cab0cd1089a189d607d296c31ddb1bc0/pics/movie/share_g.png"
                alt="去绑定新浪微博" />去绑定新浪微博</a>

</div>

<style type="text/css">
    .sync-setting {
        float: left;
    }
    #lnk-sync-setting,
    #lnk-sync-setting:hover,
    #lnk-sync-setting:visited {
        vertical-align: middle;
        color: #0192b5;
        background: none;
        line-height: 27px;
        margin-right: 8px;
    }
    #lnk-sync-setting img {
        vertical-align: baseline;
        *vertical-align: middle;
        opacity: .5;
        filter: alpha(opacity=50);
        display: inline-block;
        width: 10px;
        height: 10px;
        *display: inline;
        zoom: 1;
        position: relative;
        top: 1px;
        margin-left: 5px;
    }
    #lnk-sync-setting:hover img {
        opacity: .8;
        background: none;
        filter: alpha(opacity=80);
    }
    .share-label {
        margin: 8px;
        cursor: pointer;
        vertical-align: middle;
        *vertical-align: text-bottom;
    }
    .interest-form-ft .share-label input {
        margin-bottom: 0;
    }
    .interest-form-ft {
        text-align: right;
    }
    .interest-form-ft .bn-flat {
        float: none;
    }
    .interest-form-ft .sync-setting {
        float: left;
        line-height: 25px;
    }
</style>


                <span class="avail-num-indicator">140</span>
                <span class="bn-flat">
                    <input type="submit" value="推荐" />
                </span>
            </div>
        </div>
    </form>

    <div id="suggest-mention-tmpl" style="display:none;">
        <ul>
            {{#users}}
            <li id="{{uid}}">
              <img src="{{avatar}}">{{{username}}}&nbsp;<span>({{{uid}}})</span>
            </li>
            {{/users}}
        </ul>
    </div>


    </script>


        <a href="#" data-share-dialog="#movie-share" data-dialog-title="推荐电影" class="lnk-sharing" share-id="1292052" data-mode="plain" data-name="肖申克的救赎 The Shawshank Redemption‎ (1994)" data-type="movie" data-desc="导演 弗兰克·德拉邦特 主演 蒂姆·罗宾斯 / 摩根·弗里曼 / 美国 / 9.6分(1284269评价)" data-href="https://movie.douban.com/subject/1292052/" data-image="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp" data-properties="{}" data-redir="" data-text="" data-apikey="" data-curl="" data-count="10" data-object_kind="1002" data-object_id="1292052" data-target_type="rec" data-target_action="0" data-action_props="{&#34;subject_url&#34;:&#34;https:\/\/movie.douban.com\/subject\/1292052\/&#34;,&#34;subject_title&#34;:&#34;肖申克的救赎 The Shawshank Redemption‎ (1994)&#34;}">推荐</a>
</span>


</div>






            <script type="text/javascript">
                $(function() {
                    $('.collect_btn', '#interest_sect_level').each(function() {
                        Douban.init_collect_btn(this);
                    });
                    $('html').delegate(".indent .rec-sec .lnk-sharing", "click", function() {
                        moreurl(this, {
                            from : 'mv_sbj_db_share'
                        });
                    });
                });
            </script>
        </div>



    <div id="collect_form_1292052"></div>






<div class="related-info" style="margin-bottom:-10px;">
    <a name="intro"></a>




    <h2>
        <i class="">肖申克的救赎的剧情简介</i>
              · · · · · ·
    </h2>

            <div class="indent" id="link-report">

                        <span class="short">
                            <span property="v:summary">
                                    　　20世纪40年代末，小有成就的青年银行家安迪（蒂姆·罗宾斯 Tim Robbins 饰）因涉嫌杀害妻子及她的情人而锒铛入狱。在这座名为肖申克的监狱内，希望似乎虚无缥缈，终身监禁的惩罚无疑注定了安迪接下来灰暗绝望的人生。未过多久，安迪尝试接近囚犯中颇有声望的瑞德（摩根·弗里曼 Morgan Freeman 饰），请求对方帮自己搞来小锤子。以此为契机，二人逐渐熟稔，安迪也仿佛在鱼龙混杂、罪恶横生、黑白混淆的牢狱中找到属于自己的求生之道。他利用自身的专业知识，帮助监狱管理层逃税、洗黑钱，同时凭借与瑞德的交往在犯人中间也渐渐受到礼遇。表面看来，他已如瑞德那样对那堵高墙从憎恨转变为处之泰然，但是对自由的渴望仍促使他朝着心中的希望和目标前进。而关于其罪行的真相，似乎更使这一切朝前推进了一步……
                                        <br />
                                    　　本片根据著名作家斯蒂芬·金（Stephen Edwin King）的...
                            </span>
                            <a href="javascript:void(0)" class="j a_show_full">(展开全部)</a>
                        </span>
                        <span class="all hidden">                                　　20世纪40年代末，小有成就的青年银行家安迪（蒂姆·罗宾斯 Tim Robbins 饰）因涉嫌杀害妻子及她的情人而锒铛入狱。在这座名为肖申克的监狱内，希望似乎虚无缥缈，终身监禁的惩罚无疑注定了安迪接下来灰暗绝望的人生。未过多久，安迪尝试接近囚犯中颇有声望的瑞德（摩根·弗里曼 Morgan Freeman 饰），请求对方帮自己搞来小锤子。以此为契机，二人逐渐熟稔，安迪也仿佛在鱼龙混杂、罪恶横生、黑白混淆的牢狱中找到属于自己的求生之道。他利用自身的专业知识，帮助监狱管理层逃税、洗黑钱，同时凭借与瑞德的交往在犯人中间也渐渐受到礼遇。表面看来，他已如瑞德那样对那堵高墙从憎恨转变为处之泰然，但是对自由的渴望仍促使他朝着心中的希望和目标前进。而关于其罪行的真相，似乎更使这一切朝前推进了一步……
                                    <br />
                                　　本片根据著名作家斯蒂芬·金（Stephen Edwin King）的原著改编。
                        </span>
                        <span class="pl"><a href="https://movie.douban.com/help/movie#t0-qs">&copy;豆瓣</a></span>
            </div>
</div>











<div id="celebrities" class="celebrities related-celebrities">


    <h2>
        <i class="">肖申克的救赎的演职员</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="/subject/1292052/celebrities">全部 35</a>
            )
            </span>
    </h2>


  <ul class="celebrities-list from-subject __oneline">





  <li class="celebrity">


  <a href="https://movie.douban.com/celebrity/1047973/" title="弗兰克·德拉邦特 Frank Darabont" class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/view/celebrity/s_ratio_celebrity/public/p230.webp)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1047973/" title="弗兰克·德拉邦特 Frank Darabont" class="name">弗兰克·德拉邦特</a></span>

      <span class="role" title="导演">导演</span>

    </div>
  </li>







  <li class="celebrity">


  <a href="https://movie.douban.com/celebrity/1054521/" title="蒂姆·罗宾斯 Tim Robbins" class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/view/celebrity/s_ratio_celebrity/public/p17525.webp)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1054521/" title="蒂姆·罗宾斯 Tim Robbins" class="name">蒂姆·罗宾斯</a></span>

      <span class="role" title="饰 安迪·杜佛兰 Andy Dufresne">饰 安迪·杜佛兰 Andy Dufresne</span>

    </div>
  </li>







  <li class="celebrity">


  <a href="https://movie.douban.com/celebrity/1054534/" title="摩根·弗里曼 Morgan Freeman" class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/view/celebrity/s_ratio_celebrity/public/p34642.webp)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1054534/" title="摩根·弗里曼 Morgan Freeman" class="name">摩根·弗里曼</a></span>

      <span class="role" title="饰 艾利斯·波伊德·“瑞德”·瑞丁 Ellis Boyd &#39;Red&#39; Redding">饰 艾利斯·波伊德·“瑞德”·瑞丁 Ellis Boyd &#39;Red&#39; Redding</span>

    </div>
  </li>







  <li class="celebrity">


  <a href="https://movie.douban.com/celebrity/1041179/" title="鲍勃·冈顿 Bob Gunton" class="">
      <div class="avatar" style="background-image: url(https://img1.doubanio.com/view/celebrity/s_ratio_celebrity/public/p5837.webp)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1041179/" title="鲍勃·冈顿 Bob Gunton" class="name">鲍勃·冈顿</a></span>

      <span class="role" title="饰 监狱长山姆·诺顿 Warden Norton">饰 监狱长山姆·诺顿 Warden Norton</span>

    </div>
  </li>







  <li class="celebrity">


  <a href="https://movie.douban.com/celebrity/1000095/" title="威廉姆·赛德勒 William Sadler" class="">
      <div class="avatar" style="background-image: url(https://img1.doubanio.com/view/celebrity/s_ratio_celebrity/public/p7827.webp)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1000095/" title="威廉姆·赛德勒 William Sadler" class="name">威廉姆·赛德勒</a></span>

      <span class="role" title="饰 海伍德 Heywood">饰 海伍德 Heywood</span>

    </div>
  </li>







  <li class="celebrity">


  <a href="https://movie.douban.com/celebrity/1013817/" title="克兰西·布朗 Clancy Brown" class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/view/celebrity/s_ratio_celebrity/public/p11475.webp)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1013817/" title="克兰西·布朗 Clancy Brown" class="name">克兰西·布朗</a></span>

      <span class="role" title="饰 上尉哈德利 Captain Hadley">饰 上尉哈德利 Captain Hadley</span>

    </div>
  </li>


  </ul>
</div>





<link rel="stylesheet" href="https://img3.doubanio.com/f/verify/16c7e943aee3b1dc6d65f600fcc0f6d62db7dfb4/entry_creator/dist/author_subject/style.css">
<div id="author_subject" class="author-wrapper">
    <div class="loading"></div>
</div>
<script type="text/javascript">
    var answerObj = {
      ISALL: 'False',
      TYPE: 'movie',
      SUBJECT_ID: '1292052',
      USER_ID: '181757233'
    }
</script>
<script type="text/javascript" src="https://img3.doubanio.com/f/movie/61252f2f9b35f08b37f69d17dfe48310dd295347/js/movie/lib/react/15.4/bundle.js"></script>
<script type="text/javascript" src="https://img3.doubanio.com/f/verify/ac140ef86262b845d2be7b859e352d8196f3f6d4/entry_creator/dist/author_subject/index.js"></script>













    <div id="related-pic" class="related-pic">



    <h2>
        <i class="">肖申克的救赎的视频和图片</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/1292052/trailer#trailer">预告片1</a>&nbsp;|&nbsp;<a href="https://movie.douban.com/subject/1292052/trailer#short_video">视频评论2</a>&nbsp;·&nbsp;<a href="/video/create?subject_id=1292052">添加</a>&nbsp;|&nbsp;<a href="https://movie.douban.com/subject/1292052/all_photos">图片634</a>&nbsp;·&nbsp;<a href="https://movie.douban.com/subject/1292052/mupload">添加</a>
            )
            </span>
    </h2>


        <ul class="related-pic-bd  wide_videos">
                <li class="label-trailer">
                    <a class="related-pic-video" href="https://movie.douban.com/trailer/108756/#content" title="预告片" style="background-image:url(https://img3.doubanio.com/img/trailer/medium/1433841022.jpg?)">
                    </a>
                </li>

                <li class="label-short-video">
                    <a class="related-pic-video" href="https://movie.douban.com/video/100235/" title="视频评论" style="background-image:url(https://img3.doubanio.com/view/photo/photo/public/p2524242880.webp?)">
                    </a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/490571815/"><img src="https://img3.doubanio.com/view/photo/sqxs/public/p490571815.webp" alt="图片" /></a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2309770674/"><img src="https://img3.doubanio.com/view/photo/sqxs/public/p2309770674.webp" alt="图片" /></a>
                </li>
        </ul>
    </div>









<style type="text/css">
.award li { display: inline; margin-right: 5px }
.awards { margin-bottom: 20px }
.awards h2 { background: none; color: #000; font-size: 14px; padding-bottom: 5px; margin-bottom: 8px; border-bottom: 1px dashed #dddddd }
.awards .year { color: #666666; margin-left: -5px }
.mod { margin-bottom: 25px }
.mod .hd { margin-bottom: 10px }
.mod .hd h2 {margin:24px 0 3px 0}
</style>


<div class="mod">
    <div class="hd">

    <h2>
        <i class="">肖申克的救赎的获奖情况</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/1292052/awards/">全部</a>
            )
            </span>
    </h2>

    </div>

        <ul class="award">
            <li>
                <a href="https://movie.douban.com/awards/Oscar/67/">第67届奥斯卡金像奖</a>
            </li>
            <li>最佳影片(提名)</li>
            <li><a href='https://movie.douban.com/celebrity/1291197/' target='_blank'>妮基·马文</a></li>
        </ul>

        <ul class="award">
            <li>
                <a href="https://movie.douban.com/awards/jap/19/">第19届日本电影学院奖</a>
            </li>
            <li>最佳外语片</li>
            <li></li>
        </ul>

        <ul class="award">
            <li>
                <a href="https://movie.douban.com/awards/hochi/20/">第20届报知映画赏</a>
            </li>
            <li>海外作品奖</li>
            <li><a href='https://movie.douban.com/celebrity/1047973/' target='_blank'>弗兰克·德拉邦特</a></li>
        </ul>
</div>










    <div id="recommendations" class="">


    <h2>
        <i class="">喜欢这部电影的人也喜欢</i>
              · · · · · ·
    </h2>



    <div class="recommendations-bd">
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1292720/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p510876377.webp" alt="阿甘正传" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1292720/?from=subject-page" class="" >阿甘正传</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1849031/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1312700744.webp" alt="当幸福来敲门" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1849031/?from=subject-page" class="" >当幸福来敲门</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1292064/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p479682972.webp" alt="楚门的世界" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1292064/?from=subject-page" class="" >楚门的世界</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1292224/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p792238287.webp" alt="飞越疯人院" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1292224/?from=subject-page" class="" >飞越疯人院</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/2209573/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2434249040.webp" alt="贫民窟的百万富翁" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/2209573/?from=subject-page" class="" >贫民窟的百万富翁</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/3793023/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p579729551.webp" alt="三傻大闹宝莱坞" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/3793023/?from=subject-page" class="" >三傻大闹宝莱坞</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1292365/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2513253791.webp" alt="活着" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1292365/?from=subject-page" class="" >活着</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1292656/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480965695.webp" alt="心灵捕手" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1292656/?from=subject-page" class="" >心灵捕手</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1298653/?from=subject-page" >
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2207673534.webp" alt="荒岛余生" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1298653/?from=subject-page" class="" >荒岛余生</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1298624/?from=subject-page" >
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p925123037.webp" alt="闻香识女人" class="" />
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1298624/?from=subject-page" class="" >闻香识女人</a>
            </dd>
        </dl>
    </div>

    </div>






<script type="text/x-handlebar-tmpl" id="comment-tmpl">
    <div class="dummy-fold">
        {{#each comments}}
        <div class="comment-item" data-cid="id">
            <div class="comment">
                <h3>
                    <span class="comment-vote">
                            <span class="votes">{{votes}}</span>
                        <input value="{{id}}" type="hidden"/>
                        <a href="javascript:;" class="j {{#if ../if_logined}}a_vote_comment{{else}}a_show_login{{/if}}">有用</a>
                    </span>
                    <span class="comment-info">
                        <a href="{{user.path}}" class="">{{user.name}}</a>
                        {{#if rating}}
                        <span class="allstar{{rating}}0 rating" title="{{rating_word}}"></span>
                        {{/if}}
                        <span>
                            {{time}}
                        </span>
                        <p> {{content_tmpl content}} </p>
                    </span>
            </div>
        </div>
        {{/each}}
    </div>
</script>














    <div id="comments-section">
        <div class="mod-hd">

        <a class="comment_btn j a_collect_btn" name="cbtn-1292052" href="javascript:;" rel="nofollow">
            <span>我要写短评</span>
        </a>



    <h2>
        <i class="">肖申克的救赎的短评</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/1292052/comments?status=P">全部 256156 条</a>
            )
            </span>
    </h2>

        </div>
        <div class="mod-bd">

    <div class="tab-hd">
        <a id="hot-comments-tab" href="comments" data-id="hot" class="on">热门</a>&nbsp;/&nbsp;
        <a id="new-comments-tab" href="comments?sort=time" data-id="new">最新</a>&nbsp;/&nbsp;
        <a id="following-comments-tab" href="follows_comments" data-id="following" >好友</a>
    </div>

    <div class="tab-bd">
        <div id="hot-comments" class="tab">



        <div class="comment-item" data-cid="2050003">


    <div class="comment">
        <h3>
            <span class="comment-vote">
                <span class="votes">20696</span>
                <input value="2050003" type="hidden"/>
                <a href="javascript:;" class="j a_vote_comment" onclick="">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/kingfish/" class="">kingfish</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2006-03-22 12:38:09">
                    2006-03-22
                </span>
            </span>
        </h3>
        <p class="">

                <span class="short">不需要女主角的好电影</span>
        </p>
    </div>

        </div>

        <div class="comment-item" data-cid="40114704">


    <div class="comment">
        <h3>
            <span class="comment-vote">
                <span class="votes">5127</span>
                <input value="40114704" type="hidden"/>
                <a href="javascript:;" class="j a_vote_comment" onclick="">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/eve42/" class="">Eve|Classified</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2008-05-09 23:15:34">
                    2008-05-09
                </span>
            </span>
        </h3>
        <p class="">

                <span class="short">“这是一部男人必看的电影。”人人都这么说。但单纯从性别区分，就会让这电影变狭隘。《肖申克的救赎》突破了男人电影的局限，通篇几乎充满令人难以置信的温馨基调，而电影里最伟大的主题是“希望”。
当我们无奈地遇到了如同肖申克一般囚禁了心灵自由的那种囹圄，我们是无奈的老布鲁克，灰心的瑞德，还是智慧的安迪？运用智慧，信任希望，并且勇敢面对恐惧心理，去打败它？
经典的电影之所以经典，因为他们都在做同一件事—...</span>
                <span class="hide-item full">“这是一部男人必看的电影。”人人都这么说。但单纯从性别区分，就会让这电影变狭隘。《肖申克的救赎》突破了男人电影的局限，通篇几乎充满令人难以置信的温馨基调，而电影里最伟大的主题是“希望”。
当我们无奈地遇到了如同肖申克一般囚禁了心灵自由的那种囹圄，我们是无奈的老布鲁克，灰心的瑞德，还是智慧的安迪？运用智慧，信任希望，并且勇敢面对恐惧心理，去打败它？
经典的电影之所以经典，因为他们都在做同一件事——让你从不同的角度来欣赏希望的美好。</span>
                <span class="expand">(<a href="javascript:;">展开</a>)</span>
        </p>
    </div>

        </div>

        <div class="comment-item" data-cid="980059">


    <div class="comment">
        <h3>
            <span class="comment-vote">
                <span class="votes">3748</span>
                <input value="980059" type="hidden"/>
                <a href="javascript:;" class="j a_vote_comment" onclick="">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/zyl622/" class="">寂地</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2006-01-02 23:57:15">
                    2006-01-02
                </span>
            </span>
        </h3>
        <p class="">

                <span class="short">超级喜欢超级喜欢,不看的话人生不圆满.</span>
        </p>
    </div>

        </div>

        <div class="comment-item" data-cid="7096858">


    <div class="comment">
        <h3>
            <span class="comment-vote">
                <span class="votes">1056</span>
                <input value="7096858" type="hidden"/>
                <a href="javascript:;" class="j a_vote_comment" onclick="">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/jennyqueen/" class="">珍妮的肖像</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2006-11-13 08:41:13">
                    2006-11-13
                </span>
            </span>
        </h3>
        <p class="">

                <span class="short">没有人会不喜欢吧！书和电影都好。</span>
        </p>
    </div>

        </div>

        <div class="comment-item" data-cid="537314500">


    <div class="comment">
        <h3>
            <span class="comment-vote">
                <span class="votes">931</span>
                <input value="537314500" type="hidden"/>
                <a href="javascript:;" class="j a_vote_comment" onclick="">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/mmysl/" class="">葱</a>
                    <span>看过</span>
                    <span class="allstar50 rating" title="力荐"></span>
                <span class="comment-time " title="2012-05-28 22:57:42">
                    2012-05-28
                </span>
            </span>
        </h3>
        <p class="">

                <span class="short">这样的男人谁会舍得背叛。。。</span>
        </p>
    </div>

        </div>




                &gt; <a href="comments?sort=new_score&status=P" >更多短评256156条</a>
        </div>
        <div id="new-comments" class="tab">
            <div id="normal">
            </div>
            <div class="fold-hd hide">
                <a class="qa" href="/help/opinion#t2-q0" target="_blank">为什么被折叠？</a>
                <a class="btn-unfold" href="#">有一些短评被折叠了</a>
                <div class="qa-tip">
                    评论被折叠，是因为发布这条评论的帐号行为异常。评论仍可以被展开阅读，对发布人的账号不造成其他影响。如果认为有问题，可以<a href="https://help.douban.com/help/ask?category=movie">联系</a>豆瓣电影。
                </div>
            </div>
            <div class="fold-bd">
            </div>
            <span id="total-num"></span>
        </div>
        <div id="following-comments" class="tab">




        <div class="comment-item">
            你关注的人还没写过短评
        </div>

        </div>
    </div>




        </div>
    </div>





<link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/73ed658484f98d44.css">

<section class="topics mod">
    <header>
        <h2>
            肖申克的救赎的话题 · · · · · ·
            <span class="pl">( <span class="gallery_topics">全部 <span id="topic-count"></span> 条</span> )</span>
        </h2>
    </header>






<section class="subject-topics">
    <div class="topic-guide" id="topic-guide">
        <img class="ic_question" src="//img3.doubanio.com/f/ithildin/b1a3edea3d04805f899e9d77c0bfc0d158df10d5/pics/export/icon_question.png">
        <div class="tip_content">
            <div class="tip_title">什么是话题</div>
            <div class="tip_desc">
                <div>无论是一部作品、一个人，还是一件事，都往往可以衍生出许多不同的话题。将这些话题细分出来，分别进行讨论，会有更多收获。</div>
            </div>
        </div>
        <img class="ic_guide" src="//img3.doubanio.com/f/ithildin/529f46d86bc08f55cd0b1843d0492242ebbd22de/pics/export/icon_guide_arrow.png">
        <img class="ic_close" id="topic-guide-close" src="//img3.doubanio.com/f/ithildin/2eb4ad488cb0854644b23f20b6fa312404429589/pics/export/close@3x.png">
    </div>

    <div id="topic-items"></div>

    <script>
        window.subject_id = 1292052;
        window.join_label_text = '写影评参与';

        window.topic_display_count = 4;
        window.topic_item_display_count = 1;
        window.no_content_fun_call_name = "no_topic";

        window.guideNode = document.getElementById('topic-guide');
        window.guideNodeClose = document.getElementById('topic-guide-close');
    </script>

        <link rel="stylesheet" href="https://img3.doubanio.com/f/ithildin/f731c9ea474da58c516290b3a6b1dd1237c07c5e/css/export/subject_topics.css">
        <script src="https://img3.doubanio.com/f/ithildin/d3590fc6ac47b33c804037a1aa7eec49075428c8/js/export/moment-with-locales-only-zh.js"></script>
        <script src="https://img3.doubanio.com/f/ithildin/c600fdbe69e3ffa5a3919c81ae8c8b4140e99a3e/js/export/subject_topics.js"></script>

</section>

    <script>
        function no_topic(){
            $('#content .topics').remove();
        }
    </script>
</section>

<section class="reviews mod movie-content">
    <header>
        <a href="new_review" rel="nofollow" class="create-review comment_btn"
            data-isverify="True"
            data-verify-url="https://www.douban.com/accounts/phone/verify?redir=http://movie.douban.com/subject/1292052/new_review">
            <span>我要写影评</span>
        </a>
        <h2>
            肖申克的救赎的影评 · · · · · ·
            <span class="pl">( <a href="reviews">全部 7369 条</a> )</span>
        </h2>
    </header>



<style>
#gallery-topics-selection {
  position: fixed;
  width: 595px;
  padding: 40px 40px 33px 40px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 16px 0 rgba(0, 0, 0, 0.2);
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  z-index: 9999;
}
#gallery-topics-selection h1 {
  font-size: 18px;
  color: #007722;
  margin-bottom: 36px;
  padding: 0;
  line-height: 28px;
  font-weight: normal;
}
#gallery-topics-selection .gl_topics {
  border-bottom: 1px solid #dfdfdf;
  max-height: 298px;
  overflow-y: scroll;
}
#gallery-topics-selection .topic {
  margin-bottom: 24px;
}
#gallery-topics-selection .topic_name {
  font-size: 15px;
  color: #333;
  margin: 0;
  line-height: inherit;
}
#gallery-topics-selection .topic_meta {
  font-size: 13px;
  color: #999;
}
#gallery-topics-selection .topics_skip {
  display: block;
  cursor: pointer;
  font-size: 16px;
  color: #3377AA;
  text-align: center;
  margin-top: 33px;
}
#gallery-topics-selection .topics_skip:hover {
  background: transparent;
}
#gallery-topics-selection .close_selection {
  position: absolute;
  width: 30px;
  height: 20px;
  top: 46px;
  right: 40px;
  background: #fff;
  color: #999;
  text-align: right;
}
#gallery-topics-selection .close_selection:hover{
  background: #fff;
  color: #999;
}
</style>




        <div class="review_filter">
            <a href="javascript:;;" class="cur" data-sort="">热门</a href="javascript:;;"> /
            <a href="javascript:;;" data-sort="time">最新</a href="javascript:;;"> /
            <a href="javascript:;;" data-sort="follow">好友</a href="javascript:;;">

        </div>






<div class="review-list  ">





    <div data-cid="1000369">
        <div class="main review-item" id="1000369">



    <header class="main-hd">
        <a href="https://www.douban.com/people/bighead/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u1000152-23.jpg">
        </a>

        <a href="https://www.douban.com/people/bighead/" class="name">大头绿豆</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2005-05-12" class="main-meta">2005-05-12 20:44:13</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/1000369/">十年·肖申克的救赎</a></h2>

                <div id="review_1000369_short" class="review-short" data-rid="1000369">
                    <div class="short-content">

                        距离斯蒂芬·金（Stephen King）和德拉邦特（Frank Darabont）们缔造这部伟大的作品已经有十年了。我知道美好的东西想必大家都能感受，但是很抱歉，我的聒噪仍将一如既往。 在我眼里，肖申克的救赎与信念、自由和友谊有关。 ［1］信 念 瑞德（Red）说，希望是危险的东西，是精...

                        &nbsp;(<a href="javascript:;" id="toggle-1000369-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1000369_full" class="hidden">
                    <div id="review_1000369_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1000369" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1000369">
                                13679
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1000369" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1000369">
                                667
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/1000369/#comments" class="reply">768回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>



    <div data-cid="1001258">
        <div class="main review-item" id="1001258">



    <header class="main-hd">
        <a href="https://www.douban.com/people/lazywormzhao/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u1000564-1.jpg">
        </a>

        <a href="https://www.douban.com/people/lazywormzhao/" class="name">隱居雲上</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2005-07-12" class="main-meta">2005-07-12 11:23:39</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/1001258/">终于找到了郁闷人生的原因――观《肖申克的救赎》有感</a></h2>

                <div id="review_1001258_short" class="review-short" data-rid="1001258">
                    <div class="short-content">

                         周末看了一部美国影片《肖申克的救赎》（《The Shawshank Redemption》） 讲的是一位因冤案入狱的年轻银行家在牢中如何追寻自由的故事。 不同的人看同样的影片可能都有不同的感受。对于目前无力改变现状的我，看完这部影片后最深的感受就是：才华、毅力两样，是任何人在任何境...

                        &nbsp;(<a href="javascript:;" id="toggle-1001258-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1001258_full" class="hidden">
                    <div id="review_1001258_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1001258" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1001258">
                                8937
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1001258" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1001258">
                                735
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/1001258/#comments" class="reply">594回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>



    <div data-cid="1208594">
        <div class="main review-item" id="1208594">



    <header class="main-hd">
        <a href="https://www.douban.com/people/1817888/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u1817888-4.jpg">
        </a>

        <a href="https://www.douban.com/people/1817888/" class="name">中原狮子王</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2007-09-15" class="main-meta">2007-09-15 22:59:08</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/1208594/">《肖申克的救赎》与斯德哥尔摩综合症－－你我都是患者！</a></h2>

                <div id="review_1208594_short" class="review-short" data-rid="1208594">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                           斯德哥尔摩综合症（Stockholm syndrome），斯德哥尔摩效应，又称斯德哥尔摩症候群或者称为人质情结或人质综合症，是指犯罪的被害者对于犯罪者产生情感，甚至反过来帮助犯罪者的一种情结。这个情感造成被害人对加害人产生好感、依赖心、甚至协助加害人。  　　1973年8月23日...

                        &nbsp;(<a href="javascript:;" id="toggle-1208594-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1208594_full" class="hidden">
                    <div id="review_1208594_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1208594" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1208594">
                                5638
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1208594" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1208594">
                                834
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/1208594/#comments" class="reply">534回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>



    <div data-cid="1019121">
        <div class="main review-item" id="1019121">



    <header class="main-hd">
        <a href="https://www.douban.com/people/nakedfake/" class="avator">
            <img width="24" height="24" src="https://img1.doubanio.com/icon/user_normal.jpg">
        </a>

        <a href="https://www.douban.com/people/nakedfake/" class="name">[已注销]</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2006-01-07" class="main-meta">2006-01-07 20:56:26</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/1019121/">Andy Dufresne</a></h2>

                <div id="review_1019121_short" class="review-short" data-rid="1019121">
                    <div class="short-content">

                        Andy Dufresne，一个永垂电影史册的名字。  1  关于《The Shawshank Redemption》的评论，太多，该说的差不多都已说了千万遍。对于这样一个热门的话题，再想要抒发一些个人的喜爱之情，不免有拾人牙慧之嫌。为了避免这样没新意的事情发生，许多单词我就不再提了，譬如“希望”...

                        &nbsp;(<a href="javascript:;" id="toggle-1019121-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1019121_full" class="hidden">
                    <div id="review_1019121_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1019121" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1019121">
                                2938
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1019121" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1019121">
                                102
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/1019121/#comments" class="reply">228回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>



    <div data-cid="1127585">
        <div class="main review-item" id="1127585">



    <header class="main-hd">
        <a href="https://www.douban.com/people/1317870/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u1317870-33.jpg">
        </a>

        <a href="https://www.douban.com/people/1317870/" class="name">aratana</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2007-02-26" class="main-meta">2007-02-26 10:38:45</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/1127585/">《肖申克的救赎》：1994—2007，希望就是现实</a></h2>

                <div id="review_1127585_short" class="review-short" data-rid="1127585">
                    <div class="short-content">

                        一、缘起  从来没想过给《肖申克的救赎》写一篇影评，也许是生怕暴露自己只是个不谙世事的初级影迷，也许是对这样一部无法复制的影片真的不愿去过多地提起。然而一场出其不意的重感冒让我只能卧床裹被，已没有了力气去消化我那些故作高深、一直收着却懒得去看的电影，不期然地...

                        &nbsp;(<a href="javascript:;" id="toggle-1127585-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1127585_full" class="hidden">
                    <div id="review_1127585_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1127585" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1127585">
                                1585
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1127585" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1127585">
                                151
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/1127585/#comments" class="reply">173回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>



    <div data-cid="9259304">
        <div class="main review-item" id="9259304">



    <header class="main-hd">
        <a href="https://www.douban.com/people/yalindongdong/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u2586116-96.jpg">
        </a>

        <a href="https://www.douban.com/people/yalindongdong/" class="name">方枪枪</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2018-03-30" class="main-meta">2018-03-30 16:46:05</span>

            <a class="rel-topic" target="_blank" href="//www.douban.com/gallery/topic/为何《肖申克的救赎》在IMDb和豆瓣都能排第一？">#为何《肖申克的救赎》在IMDb和豆瓣都能排第一？</a>

    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/9259304/">为何《肖申克的救赎》在IMDb和豆瓣都能排第一？</a></h2>

                <div id="review_9259304_short" class="review-short" data-rid="9259304">
                    <div class="short-content">

                        时间会证明经典的价值，虽然在某些时刻会被误判和忽视。 用上面这句话来描述电影《肖申克的救赎》丝毫不会让人觉得会有任何夸张和吹捧的意味，因为这部电影在后来多年牢牢占据IMDB和豆瓣电影榜单第一名的位置足以说明一切。但就是这么一部经典的电影，却在其锋芒初露的时候被人...

                        &nbsp;(<a href="javascript:;" id="toggle-9259304-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_9259304_full" class="hidden">
                    <div id="review_9259304_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="9259304" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-9259304">
                                3344
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="9259304" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-9259304">
                                686
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/9259304/#comments" class="reply">374回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>



    <div data-cid="1005528">
        <div class="main review-item" id="1005528">



    <header class="main-hd">
        <a href="https://www.douban.com/people/suoliweng/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u1026935-2.jpg">
        </a>

        <a href="https://www.douban.com/people/suoliweng/" class="name">蓑笠翁</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2005-09-25" class="main-meta">2005-09-25 16:27:41</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/1005528/">人生的过程就是一个摆脱institutionalization(体制化)的过程</a></h2>

                <div id="review_1005528_short" class="review-short" data-rid="1005528">
                    <div class="short-content">

                        现在好象比较时兴将人分为体制内和体制外的人,体制外的人通常有某种优越感,似乎自己的人格才是独立的.可实际上,真正愿意做体制外的人还是很少的,而且是很痛苦的.余杰北大硕士毕业后差一点进了他想进的国家图书馆作一个体制内的人,可由于他写了一些比较反体制的文章,最后还是被...

                        &nbsp;(<a href="javascript:;" id="toggle-1005528-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1005528_full" class="hidden">
                    <div id="review_1005528_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1005528" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1005528">
                                847
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1005528" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1005528">
                                64
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/1005528/#comments" class="reply">118回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>



    <div data-cid="1062920">
        <div class="main review-item" id="1062920">



    <header class="main-hd">
        <a href="https://www.douban.com/people/erichuang/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u1187841-1.jpg">
        </a>

        <a href="https://www.douban.com/people/erichuang/" class="name">油爆虾</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2006-08-03" class="main-meta">2006-08-03 23:24:54</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/1062920/">《肖申克的救赎》的一些幕后花絮</a></h2>

                <div id="review_1062920_short" class="review-short" data-rid="1062920">
                    <div class="short-content">

                         * 是否记得片尾有一行字幕&#34;In memory of Allen Greene&#34;？翻译成中文就是&#34;纪念Allen Greene &#34;。Allen Greene是《肖申克的救赎》编导Frank Darabont的经纪人，在影片完成 的前夕死于AIDS的并发症。 　　 　　* 是否记得刚来到监狱的新囚犯们走下囚车时，嘲笑他们的人群中有一个...

                        &nbsp;(<a href="javascript:;" id="toggle-1062920-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1062920_full" class="hidden">
                    <div id="review_1062920_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1062920" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1062920">
                                466
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1062920" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1062920">
                                36
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/1062920/#comments" class="reply">40回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>



    <div data-cid="8649949">
        <div class="main review-item" id="8649949">



    <header class="main-hd">
        <a href="https://www.douban.com/people/131064354/" class="avator">
            <img width="24" height="24" src="https://img1.doubanio.com/icon/u131064354-8.jpg">
        </a>

        <a href="https://www.douban.com/people/131064354/" class="name">好美的美好</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2017-07-07" class="main-meta">2017-07-07 15:18:50</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/8649949/">《肖申克的救赎》台词整理</a></h2>

                <div id="review_8649949_short" class="review-short" data-rid="8649949">
                    <div class="short-content">

                        1．It takes a strong man to save himself, and a great man to save another. 强者救赎自己，圣人普度他人 2．Hope is a good thing, maybe the best of things, and no good thing ever dies. 希望是美好的，也许是人间至善，而美好的事物永不消逝。 3．I find I&#39;m so excit...

                        &nbsp;(<a href="javascript:;" id="toggle-8649949-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_8649949_full" class="hidden">
                    <div id="review_8649949_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="8649949" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-8649949">
                                598
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="8649949" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-8649949">
                                23
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/8649949/#comments" class="reply">13回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>



    <div data-cid="8848890">
        <div class="main review-item" id="8848890">



    <header class="main-hd">
        <a href="https://www.douban.com/people/167539095/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u167539095-1.jpg">
        </a>

        <a href="https://www.douban.com/people/167539095/" class="name">豆瓣的宇宙</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2017-10-05" class="main-meta">2017-10-05 22:18:05</span>

            <a class="rel-topic" target="_blank" href="//www.douban.com/gallery/topic/《肖申克的救赎》到底“救赎”了什么？">#《肖申克的救赎》到底“救赎”了什么？</a>

    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/8848890/">关于“救赎”</a></h2>

                <div id="review_8848890_short" class="review-short" data-rid="8848890">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        个人感觉，《肖申克的救赎》（The Shawshank Redemption）中的Redemption的意思是“赎回;偿还;补救”，因此“救赎”非常完美地解释了这部电影的主题，围绕“救赎”主题的是： 1，安迪对自己的救赎：从一开始不让自己沦陷于监狱生活（对比于和他同时入狱的胖子第一晚就受不了）...

                        &nbsp;(<a href="javascript:;" id="toggle-8848890-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_8848890_full" class="hidden">
                    <div id="review_8848890_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="8848890" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-8848890">
                                857
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="8848890" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-8848890">
                                81
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/8848890/#comments" class="reply">8回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>








    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/73b16b7ecf259fae.js"></script>
    <!-- COLLECTED CSS -->
</div>








            <p class="pl">
                &gt;
                <a href="reviews">
                    更多影评7369篇
                </a>
            </p>
</section>

<!-- COLLECTED JS -->

    <br/>

        <div class="section-discussion">

                <div class="mod-hd">
                        <a class="comment_btn" href="/subject/1292052/discussion/create" rel="nofollow"><span>添加新讨论</span></a>

    <h2>
        讨论区
         &nbsp; &middot;&nbsp; &middot;&nbsp; &middot;&nbsp; &middot;&nbsp; &middot;&nbsp; &middot;
    </h2>

                </div>

  <table class="olt"><tr><td><td><td><td></tr>

        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/1292052/discussion/24036422/" title="这是我见过最让人恶心的电影！！">这是我见过最让人恶心的电影！！</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/2099608/">人肉叉烧包邮哦</a></td>
          <td class="pl"><span>401 回应</span></td>
          <td class="pl"><span>2019-01-27</span></td>
        </tr>

        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/1292052/discussion/615941713/" title="越狱真的可行？">越狱真的可行？</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/39572470/">一休妹妹呀</a></td>
          <td class="pl"><span>1 回应</span></td>
          <td class="pl"><span>2019-01-26</span></td>
        </tr>

        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/1292052/discussion/615951369/" title="要么赶着去死，要么忙于生存">要么赶着去死，要么忙于生存</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/190578506/">￡</a></td>
          <td class="pl"><span></span></td>
          <td class="pl"><span>2019-01-26</span></td>
        </tr>

        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/1292052/discussion/615260549/" title="想知道为什么有900多人打差评">想知道为什么有900多人打差评</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/158008597/">昼夜</a></td>
          <td class="pl"><span>21 回应</span></td>
          <td class="pl"><span>2019-01-26</span></td>
        </tr>

        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/1292052/discussion/615726859/" title="日本的白鸟由荣11年成功越狱4次，比之安迪如何？">日本的白鸟由荣11年成功越狱4次，比之安迪如何？</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/182755159/">Hahacat</a></td>
          <td class="pl"><span>3 回应</span></td>
          <td class="pl"><span>2019-01-25</span></td>
        </tr>
  </table>

                <p class="pl" align="right">
                    <a href="/subject/1292052/discussion/" rel="nofollow">
                        &gt; 去这部影片的讨论区（全部944条）
                    </a>
                </p>
        </div>










<div id="askmatrix">
    <div class="mod-hd">
        <h2>
            关于《肖申克的救赎》的问题
            · · · · · ·
            <span class="pl">
                (<a href='https://movie.douban.com/subject/1292052/questions/?from=subject'>
                    全部82个
                </a>)
            </span>
        </h2>




    <a class=' comment_btn'
        href='https://movie.douban.com/subject/1292052/questions/ask/?from=subject'>我来提问</a>

    </div>

    <div class="mod-bd">
        <ul class="">
            <li class="">
                <span class="tit">
                    <a href="https://movie.douban.com/subject/1292052/questions/164/?from=subject" class="">
                            为什么这部电影的评价如此之高？
                    </a>
                </span>
                <span class="meta">
                    35人回答
                </span>
            </li>
            <li class="">
                <span class="tit">
                    <a href="https://movie.douban.com/subject/1292052/questions/3982/?from=subject" class="">
                            Andy为什么不凿好隧道就逃走？
                    </a>
                </span>
                <span class="meta">
                    13人回答
                </span>
            </li>
        </ul>

        <p>&gt;
            <a href='https://movie.douban.com/subject/1292052/questions/?from=subject'>
                全部82个问题
            </a>
        </p>

    </div>
</div>






    <script type="text/javascript">
        $(function(){if($.browser.msie && $.browser.version == 6.0){
            var $info = $('#info'),
                maxWidth = parseInt($info.css('max-width'));
            if($info.width() > maxWidth) {
                $info.width(maxWidth);
            }
        }});
    </script>


            </div>
            <div class="aside">





















<script id="episode-tmpl" type="text/x-jsrender">
<div id="tv-play-source" class="play-source">
    <div class="cross">
        <span style="color:#494949; font-size:16px">{{:cn}}</span>
        <span style="cursor:pointer">✕</span>
    </div>
    <div class="episode-list">
        {{for playlist}}
            <a href="{{:play_link}}&episode={{:ep}}" target="_blank">{{:ep}}集</a>
        {{/for}}
     <div>
 </div>
</script>

<div class="gray_ad">

    <h2>
        在哪儿看这部电影
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
    </h2>

        <a href="/subject/1292052/report_subject_error?pname=在线观看" target="_blank" rel="nofollow" class="report-error">报错</a>

    <ul class="bs">
                <li>
                        <a class="playBtn" data-cn="腾讯视频" href="https://www.douban.com/link2/?url=http%3A%2F%2Fv.qq.com%2Fx%2Fcover%2F1o29ui77e85grdr.html%3Fptag%3Ddouban.movie&amp;subtype=1&amp;type=online-video" target="_blank">
                            腾讯视频
                        </a>
                    <span class="buylink-price"><span>
                        VIP免费观看
                    </span></span>
                </li>

    </ul>
</div>


    <!-- douban ad begin -->
    <div id="dale_movie_subject_top_right"></div>
    <div id="dale_movie_subject_top_middle"></div>
    <!-- douban ad end -->





<style type="text/css">
    .m4 {margin-bottom:8px; padding-bottom:8px;}
    .movieOnline {background:#FFF6ED; padding:10px; margin-bottom:20px;}
    .movieOnline h2 {margin:0 0 5px;}
    .movieOnline .sitename {line-height:2em; width:160px;}
    .movieOnline td,.movieOnline td a:link,.movieOnline td a:visited{color:#666;}
    .movieOnline td a:hover {color:#fff;}
    .link-bt:link,
    .link-bt:visited,
    .link-bt:hover,
    .link-bt:active {margin:5px 0 0; padding:2px 8px; background:#a8c598; color:#fff; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; display:inline-block;}
</style>

    <div class="gray_ad">

    <h2>
        本片原声正在播放
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
    </h2>

        <a target="_blank" href="https://music.douban.com/subject/26799887/">去豆瓣音乐收听</a>

    </div>











    <div class="tags">


    <h2>
        <i class="">豆瓣成员常用的标签</i>
              · · · · · ·
    </h2>

        <div class="tags-body">
                <a href="/tag/经典" class="">经典</a>
                <a href="/tag/励志" class="">励志</a>
                <a href="/tag/信念" class="">信念</a>
                <a href="/tag/自由" class="">自由</a>
                <a href="/tag/人性" class="">人性</a>
                <a href="/tag/美国" class="">美国</a>
                <a href="/tag/人生" class="">人生</a>
                <a href="/tag/剧情" class="">剧情</a>
        </div>
    </div>


    <div id="dale_movie_subject_inner_middle"></div>
    <div id="dale_movie_subject_download_middle"></div>









<div id="subject-doulist">


    <h2>
        <i class="">以下豆列推荐</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/1292052/doulists">全部</a>
            )
            </span>
    </h2>



    <ul>
            <li>
                <a href="https://www.douban.com/doulist/240962/" target="_blank">★豆瓣高分电影榜★ （上）9.7-8.6分</a>
                <span>(影志)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/107486/" target="_blank">【豆瓣五星电影集中营】(1/3)</a>
                <span>(影志)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/13370/" target="_blank">【励志电影】</a>
                <span>(影志)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/65439/" target="_blank">他们是高智商玩家</a>
                <span>(中间元素)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/225637/" target="_blank">那些和谐的腐剧，腐动画，腐电影们。</a>
                <span>(墨  尘)</span>
            </li>
    </ul>

</div>










<div id="subject-others-interests">


    <h2>
        <i class="">谁在看这部电影</i>
              · · · · · ·
    </h2>


    <ul class="">

            <li class="">
                <a href="https://www.douban.com/people/190189227/" class="others-interest-avatar">
                    <img src="https://img3.doubanio.com/icon/u190189227-1.jpg" class="pil" alt="大冰冰">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/190189227/" class="">大冰冰</a>
                    <div class="">
                        刚刚
                        看过
                        <span class="allstar50" title="力荐"></span>
                    </div>
                </div>
            </li>

            <li class="">
                <a href="https://www.douban.com/people/137962510/" class="others-interest-avatar">
                    <img src="https://img3.doubanio.com/icon/u137962510-4.jpg" class="pil" alt="우비汪汪">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/137962510/" class="">우비汪汪</a>
                    <div class="">
                        刚刚
                        看过
                        <span class="allstar40" title="推荐"></span>
                    </div>
                </div>
            </li>

            <li class="">
                <a href="https://www.douban.com/people/163728853/" class="others-interest-avatar">
                    <img src="https://img3.doubanio.com/icon/u163728853-1.jpg" class="pil" alt="秦君">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/163728853/" class="">秦君</a>
                    <div class="">
                        刚刚
                        看过
                        <span class="allstar50" title="力荐"></span>
                    </div>
                </div>
            </li>
    </ul>


    <div class="subject-others-interests-ft">

            <a href="https://movie.douban.com/subject/1292052/collections">1629999人看过</a>
                &nbsp;/&nbsp;
            <a href="https://movie.douban.com/subject/1292052/wishes">159738人想看</a>
    </div>

</div>






<!-- douban ad begin -->
<div id="dale_movie_subject_middle_right"></div>
<script type="text/javascript">
    (function (global) {
        if(!document.getElementsByClassName) {
            document.getElementsByClassName = function(className) {
                return this.querySelectorAll("." + className);
            };
            Element.prototype.getElementsByClassName = document.getElementsByClassName;

        }
        var articles = global.document.getElementsByClassName('article'),
            asides = global.document.getElementsByClassName('aside');

        if (articles.length > 0 && asides.length > 0 && articles[0].offsetHeight >= asides[0].offsetHeight) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_movie_subject_middle_right');
        }
    })(this);
</script>
<!-- douban ad end -->



    <br/>


<p class="pl">订阅肖申克的救赎的评论: <br/><span class="feed">
    <a href="https://movie.douban.com/feed/subject/1292052/reviews"> feed: rss 2.0</a></span></p>


            </div>
            <div class="extra">


<!-- douban ad begin -->
<div id="dale_movie_subject_bottom_super_banner"></div>
<script type="text/javascript">
    (function (global) {
        var body = global.document.body,
            html = global.document.documentElement;

        var height = Math.max(body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight);
        if (height >= 2000) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_movie_subject_bottom_super_banner');
        }
    })(this);
</script>
<!-- douban ad end -->


            </div>
        </div>
    </div>


    <div id="footer">
            <div class="footer-extra"></div>

<span id="icp" class="fleft gray-link">
    &copy; 2005－2019 douban.com, all rights reserved 北京豆网科技有限公司
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about?policy=disclaimer">免责声明</a>

    · <a href="https://help.douban.com/?app=movie" target="_blank">帮助中心</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
</span>

    </div>

    </div>
    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/7afe82d32e8fa712.js"></script>









<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = '//erebor.douban.com/',
            userId = '181757233',
            browserId = 'B6Hw_MuCGqY',
            criteria = '7:克兰西·布朗|7:马克·罗斯顿|7:詹姆斯·惠特摩|7:犯罪|7:保罗·麦克兰尼|7:鲍勃·冈顿|7:励志|7:剧情|7:信念|7:拉里·布兰登伯格|7:布赖恩·利比|7:经典|7:人生|7:威廉姆·赛德勒|7:弗兰克·梅德拉诺|7:摩根·弗里曼|7:约瑟夫·劳格诺|7:杰弗里·德曼|7:阿方索·弗里曼|7:芮妮·布莱恩|7:美国|7:弗兰克·德拉邦特|7:蒂姆·罗宾斯|7:希望|7:人性|7:自由|7:1994|7:大卫·普罗瓦尔|7:吉尔·贝罗斯|7:祖德·塞克利拉|7:V·J·福斯特|7:尼尔·吉恩托利|3:/subject/1292052/',
            preview = '',
            debug = false,
            adSlots = ['dale_movie_subject_top_icon', 'dale_movie_subject_top_right', 'dale_movie_subject_top_middle', 'dale_movie_subject_inner_middle', 'dale_movie_subject_download_middle'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', 'https://img3.doubanio.com/f/adjs/dd37385211bc8deb01376096bfa14d2c0436a98c/ad.release.js');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>






















<script type="text/javascript">
var _paq = _paq || [];
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript';
    g.defer=true;
    g.async=true;
    g.src=p+'://img3.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
})();
</script>

<script type="text/javascript">
var setMethodWithNs = function(namespace) {
  var ns = namespace ? namespace + '.' : ''
    , fn = function(string) {
        if(!ns) {return string}
        return ns + string
      }
  return fn
}

var gaWithNamespace = function(fn, namespace) {
  var method = setMethodWithNs(namespace)
  fn.call(this, method)
}

var _gaq = _gaq || []
  , accounts = [
      { id: 'UA-7019765-1', namespace: 'douban' }
    , { id: 'UA-7019765-19', namespace: '' }
    ]
  , gaInit = function(account) {
      gaWithNamespace(function(method) {
        gaInitFn.call(this, method, account)
      }, account.namespace)
    }
  , gaInitFn = function(method, account) {
      _gaq.push([method('_setAccount'), account.id]);
      _gaq.push([method('_setSampleRate'), '5']);


  _gaq.push([method('_addOrganic'), 'google', 'q'])
  _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
  _gaq.push([method('_addOrganic'), 'soso', 'w'])
  _gaq.push([method('_addOrganic'), 'youdao', 'q'])
  _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
  _gaq.push([method('_addOrganic'), 'sogou', 'query'])
  if (account.namespace) {
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
    _gaq.push([method('_addIgnoredOrganic'), 'douban'])
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
    _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
  }

      if (account.namespace === 'douban') {
        _gaq.push([method('_setDomainName'), '.douban.com'])
      }

        _gaq.push([method('_setCustomVar'), 1, 'responsive_view_mode', 'desktop', 3])

        _gaq.push([method('_setCustomVar'), 2, 'login_status', '1', 2]);

      _gaq.push([method('_trackPageview')])
    }

for(var i = 0, l = accounts.length; i < l; i++) {
  var account = accounts[i]
  gaInit(account)
}


;(function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
})()
</script>











    <!-- anson9-docker-->

  <script>_SPLITTEST=''</script>
</body>

</html>
"""
#url = 'https://movie.douban.com/subject/1292052/'
#data = requests.get(url).text
s=etree.HTML(htmldoc)

film=s.xpath('//*[@id="content"]/h1/span[1]/text()')
director=s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
actor=s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')
time=s.xpath('//*[@id="info"]/span[13]/text()')
print('电影名称：',film)
print('导演：',director)
print('主演：',actor)
print('片长：',time)
