# _*_ coding: utf-8 _*_
agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (BB10; Touch) AppleWebKit/537.1+ (KHTML, like Gecko) Version/10.0.0.1337 Mobile Safari/537.1+",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/37.0.2178.31",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.6) Gecko/2009011912 AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.6) Gecko/2009011912 Version/3.2.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; en) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; en-GB) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.22",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; en-us) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; es) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.22",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; fr) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.22",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; it-it) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; pt-pt) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.22",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_2; en-au) AppleWebKit/525.8+ (KHTML, like Gecko) Version/3.1 Safari/525.6",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_2; en-ca) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.18",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_2; en-us) AppleWebKit/525.7 (KHTML, like Gecko) Version/3.1 Safari/525.7",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_2; en-us) AppleWebKit/526.1+ (KHTML, like Gecko) Version/3.1 Safari/525.13",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_2; fr-fr) AppleWebKit/525.9 (KHTML, like Gecko) Version/3.1 Safari/525.9",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_2; ja-jp) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.18",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_3; es-es) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_3; hu-hu) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_3; nb-no) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.21 (KHTML, like Gecko) Version/3.1.2 Safari/525.21",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.27 (KHTML, like Gecko) Version/3.2.1 Safari/525.27",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/526.1+ (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/528.4+ (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/528.4+ (KHTML, like Gecko) Version/4.0dp1 Safari/526.11.2",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; fr-fr) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; fr-fr) AppleWebKit/527.2+ (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; ko-kr) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; nb-no) AppleWebKit/528.1+ (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; en-us) AppleWebKit/525.25 (KHTML, like Gecko) Version/3.2 Safari/525.25",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; en-us) AppleWebKit/528.7+ (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; it-it) AppleWebKit/525.18 (KHTML, like Gecko)",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; ja-jp) AppleWebKit/525.26.2 (KHTML, like Gecko) Version/3.2 Safari/525.26.12",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; pl-pl) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; sv-se) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; sv-se) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; de-de) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-gb) AppleWebKit/528.10+ (KHTML, like Gecko) Version/4.0dp1 Safari/526.11.2",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-gb) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit /530.1+ (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Safari/525.20",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/528.16 (KHTML, like Gecko)",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/528.4+ (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/530.0+ (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/530.1+ (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/530.1+ (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/530.6+ (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/530.6+ (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/530.7+ (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; es-es) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; fr-ca) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; fr-fr) AppleWebKit/530.5+ (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; hr-hr) AppleWebKit/530.1+ (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; ko-kr) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; ru-ru) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; ru-ru) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; de-de) AppleWebKit/525.28.3 (KHTML, like Gecko) Version/3.2.3 Safari/525.28.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/4.0.1 Safari/530.18",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; fr-fr) AppleWebKit/528.18.1 (KHTML, like Gecko) Version/4.0 Safari/528.17",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; fi-fi) AppleWebKit/531.9 (KHTML, like Gecko) Version/4.0.3 Safari/531.9",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; fr-fr) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-cn) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6; en-gb) AppleWebKit/530.1 (KHTML, like Gecko) Version/4.0 Safari/530.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6; en-us) AppleWebKit/530.1 (KHTML, like Gecko) Version/4.0 Safari/530.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6; en-us) AppleWebKit/530.3 (KHTML, like Gecko) Version/4.0 Safari/530.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; de-at) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; ja-jp) AppleWebKit/531.22.7 (KHTML, like Gecko) Version/4.0.5 Safari/531.22.7",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; el-gr) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us) AppleWebKit/531.21.11 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; zh-cn) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7; en-us) AppleWebKit/533.4 (KHTML, like Gecko) Version/4.1 Safari/533.4",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/522+ (KHTML, like Gecko) Version/3.0.2 Safari/522.12",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/522.11 (KHTML, like Gecko) Version/3.0.2 Safari/522.12",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/522.11.1 (KHTML, like Gecko) Safari/419.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/522.11.1 (KHTML, like Gecko) Version/3.0.3 Safari/522.12.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/523.2+ (KHTML, like Gecko) Version/3.0.3 Safari/522.12.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/523.5+ (KHTML, like Gecko) Version/3.0.3 Safari/522.12.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/523.9+ (KHTML, like Gecko) Version/3.0.3 Safari/522.12.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-us) AppleWebKit/419.2.1 (KHTML, like Gecko) Safari/419.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-us) AppleWebKit/525.1+ (KHTML, like Gecko) Version/3.0.4 Safari/523.10",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; es-es) AppleWebKit/523.15.1 (KHTML, like Gecko) Version/3.0.4 Safari/523.15",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; fr) AppleWebKit/523.12.2 (KHTML, like Gecko) Version/3.0.4 Safari/523.12.2",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; it-IT) AppleWebKit/521.25 (KHTML, like Gecko) Safari/521.24",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; it-it) AppleWebKit/523.12.2 (KHTML, like Gecko) Version/3.0.4 Safari/523.12.2",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; ja-jp) AppleWebKit/523.12.2 (KHTML, like Gecko) Version/3.0.4 Safari/523.12.2",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; ko-kr) AppleWebKit/523.15.1 (KHTML, like Gecko) Version/3.0.4 Safari/523.15",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; ru-ru) AppleWebKit/522.11.1 (KHTML, like Gecko) Version/3.0.3 Safari/522.12.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; da-dk) AppleWebKit/531.22.7 (KHTML, like Gecko) Version/4.0.5 Safari/531.22.7",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; de) AppleWebKit/528.4+ (KHTML, like Gecko) Version/4.0dp1 Safari/526.11.2",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; de-de) AppleWebKit/533.16 (KHTML, like Gecko) Version/4.1 Safari/533.16",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; en) AppleWebKit/525.3+ (KHTML, like Gecko) Version/3.0.4 Safari/523.12.2",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; en) AppleWebKit/528.1 (KHTML, like Gecko) Version/4.0 Safari/528.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; es-es) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; fr-fr) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; it-it) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; it-it) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; ja-jp) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.18",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; ja-jp) AppleWebKit/533.16 (KHTML, like Gecko) Version/4.1 Safari/533.16",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; sv-se) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.22",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; tr) AppleWebKit/528.4+ (KHTML, like Gecko) Version/4.0dp1 Safari/526.11.2",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_2; en-gb) AppleWebKit/526+ (KHTML, like Gecko) Version/3.1 Safari/525.9",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_3; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_3; sv-se) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.0.4 Safari/523.10",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1 Safari/525.13",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_4; fr-fr) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_5; en-us) AppleWebKit/525.26.2 (KHTML, like Gecko) Version/3.2 Safari/525.26.12",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_5; fi-fi) AppleWebKit/525.26.2 (KHTML, like Gecko) Version/3.2 Safari/525.26.12",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_5; fr-fr) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_6; en-us) AppleWebKit/528.16 (KHTML, like Gecko)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_6; en-us) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_6; en-us) AppleWebKit/530.1+ (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_6; en-us) AppleWebKit/530.9+ (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_6; it-it) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_6; ja-jp) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_6; nl-nl) AppleWebKit/530.0+ (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_6; tr-TR) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_7; en-us) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; en-us) AppleWebKit/531.22.7 (KHTML, like Gecko) Version/4.0.5 Safari/531.22.7",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ca-es) AppleWebKit/522.11.1 (KHTML, like Gecko) Version/3.0.3 Safari/522.12.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-CH) AppleWebKit/419.2 (KHTML, like Gecko) Safari/419.3",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/124 (KHTML, like Gecko) Safari/125",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/124 (KHTML, like Gecko) Safari/125.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.7",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/125.5.5 (KHTML, like Gecko) Safari/125.12_Adobe",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/125.5.6 (KHTML, like Gecko) Safari/125.12",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/312.8 (KHTML, like Gecko) Safari/312.5",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/412.6 (KHTML, like Gecko)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/412.6 (KHTML, like Gecko) Safari/412.2",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/412.6 (KHTML, like Gecko) Safari/412.2_Adobe",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/416.12 (KHTML, like Gecko) Safari/416.13_Adobe",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/419.2 (KHTML, like Gecko) Safari/419.3",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/522.11 (KHTML, like Gecko) Version/3.0.2 Safari/522.12",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/85.7 (KHTML, like Gecko) Safari/85.5",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/85.8.2 (KHTML, like Gecko) Safari/85.8",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/85.8.5 (KHTML, like Gecko) Safari/85",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.4 (KHTML, like Gecko) Safari/125.9",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.5 (KHTML, like Gecko) Safari/125.9",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.5.5 (KHTML, like Gecko) Safari/125",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.5.5 (KHTML, like Gecko) Safari/125.11",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.5.6 (KHTML, like Gecko) Safari/125.12",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.5.7 (KHTML, like Gecko) Safari/125.12",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.5.2 (KHTML, like Gecko) Safari/125",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.8 (KHTML, like Gecko) Safari/312.3.3",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.8 (KHTML, like Gecko) Safari/312.6",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/412 (KHTML, like Gecko) Safari/412",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/412.6 (KHTML, like Gecko) Safari/412.2",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/412.6.2 (KHTML, like Gecko)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/412.6.2 (KHTML, like Gecko) Safari/412.2.2",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/412.7 (KHTML, like Gecko) Safari/412.5",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/416.11 (KHTML, like Gecko)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/416.11 (KHTML, like Gecko) Safari/416.12",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/416.12 (KHTML, like Gecko) Safari/416.13",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko) Safari/419.3",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/522.11 (KHTML, like Gecko) Version/3.0.2 Safari/522.12",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/85.8.2 (KHTML, like Gecko) Safari/85.8.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/85.8.5 (KHTML, like Gecko) Safari/85.8.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-au) AppleWebKit/125.4 (KHTML, like Gecko) Safari/125.9",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-gb) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-gb) AppleWebKit/85.8.5 (KHTML, like Gecko) Safari/85.8.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/124 (KHTML, like Gecko) Safari/125",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/125.4 (KHTML, like Gecko) Safari/125.9",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/125.5.5 (KHTML, like Gecko) Safari/125.12",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/125.5.7 (KHTML, like Gecko) Safari/125.12",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.1 (KHTML, like Gecko)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.5 (KHTML, like Gecko) Safari/312.3",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.8 (KHTML, like Gecko) Safari/312.5",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.8 (KHTML, like Gecko) Safari/312.6",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/412 (KHTML, like Gecko) Safari/412",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/412.7 (KHTML, like Gecko) Safari/412.5",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/418.9 (KHTML, like Gecko) Safari/419.3",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/522+ (KHTML, like Gecko) Version/3.0.2 Safari/522.12",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/522.11 (KHTML, like Gecko) Version/3.0.2 Safari/522.12",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/523.10.3 (KHTML, like Gecko) Version/3.0.4 Safari/523.10",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/523.6 (KHTML, like Gecko) Version/3.0.3 Safari/523.6",
]


pc_agents = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
    # "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    # "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    # "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
    # "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
]


app_agents = [
    "Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-us; htc_bahamas Build/CRB17) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; HTC Desire 1.19.161.5 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 1.5; de-ch; HTC Hero Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.1; en-us; HTC Legend Build/cupcake) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 1.5; de-de; HTC Magic Build/PLAT-RC33) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 FirePHP/0.3",
    "Mozilla/5.0 (Linux; U; Android 1.6; en-us; HTC_TATTOO_A3288 Build/DRC79) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-us; T-Mobile G1 Build/CRB43) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari 525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-gb; T-Mobile_G2_Touch Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Milestone Build/ SHOLS_U2_01.03.1) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.0.1; de-de; Milestone Build/SHOLS_U2_01.14.0) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522  (KHTML, like Gecko) Safari/419.3",
    "Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-ca; GT-P1000M Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.6; en-us; SonyEricssonX10i Build/R1AA056) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
]