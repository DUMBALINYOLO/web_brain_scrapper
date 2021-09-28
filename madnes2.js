function webbraingwt() {
    var P = ''
      , xb = '" for "gwt:onLoadErrorFn"'
      , vb = '" for "gwt:onPropertyErrorFn"'
      , ib = '"><\/script>'
      , Z = '#'
      , vc = '.cache.html'
      , _ = '/'
      , lb = '//'
      
      , bc = '1B88A097E9475E16EA2232E6627C5910'
      , cc = '295CB3AA56ACACD0EFEFB310FDC7EC12'
      , dc = '305CF7DE2874011200E87F4AD1659677'
      , ec = '48D548B417791642F9DC1B0C0F1E144B'
      , fc = '5182DD1C43C6C95EA9C20622E6EF9B07'
      , kc = '5DFE00DE98349DC2D5639F7B8B13DD7B'
      , lc = '6F2FA3029EF650D049AF1D3315C55F77'
      , mc = '76A259BD45EC8F94D37E17B284F91E1A'
      , nc = '8C55A23D8CB8102181A473BC93949683'
      , oc = '9C761B16063F1539393F878302B93617'
      , pc = '9E797E366D89FC879D3180AB70837B28'
      , uc = ':'
      , ic = ':1'
      , jc = ':2'
      , pb = '::'
      , xc = '<script defer="defer">webbraingwt.onInjectionDone(\'webbraingwt\')<\/script>'
      , hb = '<script id="'
      , sb = '='
      , $ = '?'
      , qc = 'ACD08CE1DF2DF5AD0493AD00D49062A6'
      , rc = 'B31200762F476C3D80E1588C22509289'
      , sc = 'B6A42DE22B8D4225BCED6506BEB0B226'
      , ub = 'Bad handler "'
      , wc = 'DOMContentLoaded'
      , tc = 'E3F49B3E32B0AAFAA39F8C28928E83C1'
      , jb = 'SCRIPT'
      , gb = '__gwt_marker_webbraingwt'
      , Gb = 'android'
      , Ib = 'androidMobile'
      , kb = 'base'
      , cb = 'baseUrl'
      , T = 'begin'
      , S = 'bootstrap'
      , Lb = 'browser'
      , bb = 'clear.cache.gif'
      , Nb = 'column_major'
      , rb = 'content'
      , Cb = 'device.user.agent'
      , gc = 'embeddedAndroid'
      , hc = 'embeddedIOS'
      , Y = 'end'
      , Xb = 'gecko'
      , Yb = 'gecko1_8'
      , U = 'gwt.codesvr='
      , V = 'gwt.hosted='
      , W = 'gwt.hybrid'
      , wb = 'gwt:onLoadErrorFn'
      , tb = 'gwt:onPropertyErrorFn'
      , qb = 'gwt:property'
      , _b = 'hosted.html?webbraingwt'
      , Wb = 'ie6'
      , Vb = 'ie8'
      , Ub = 'ie9'
      , yb = 'iframe'
      , ab = 'img'
      , Fb = 'ipad'
      , Db = 'iphone'
      , Eb = 'ipod'
      , zb = "javascript:''"
      , $b = 'loadExternalRefs'
      , mb = 'meta'
      , Hb = 'mobile'
      , Bb = 'moduleRequested'
      , X = 'moduleStartup'
      , Tb = 'msie'
      , nb = 'name'
      , Jb = 'nexus 7'
      , Qb = 'opera'
      , Ab = 'position:absolute;width:0;height:0;border:none'
      , Ob = 'row_major'
      , Sb = 'safari'
      , db = 'script'
      , ac = 'selectingPermutation'
      , Kb = 'silk'
      , R = 'startup'
      , Mb = 'transform.notation'
      , fb = 'undefined'
      , Zb = 'unknown'
      , Pb = 'user.agent'
      , Q = 'webbraingwt'
      , eb = 'webbraingwt.nocache.js'
      , ob = 'webbraingwt::'
      , Rb = 'webkit';
    var m = window, n = document, o = m.__gwtStatsEvent ? function(a) {
        return m.__gwtStatsEvent(a)
    }
    : null, p = m.__gwtStatsSessionId ? m.__gwtStatsSessionId : null, q, r, s, t = P, u = {}, v = [], w = [], x = [], y = 0, z, A;
    o && o({
        moduleName: Q,
        sessionId: p,
        subSystem: R,
        evtGroup: S,
        millis: (new Date).getTime(),
        type: T
    });
    if (!m.__gwt_stylesLoaded) {
        m.__gwt_stylesLoaded = {}
    }
    if (!m.__gwt_scriptsLoaded) {
        m.__gwt_scriptsLoaded = {}
    }
    function B() {
        var b = false;
        try {
            var c = m.location.search;
            return (c.indexOf(U) != -1 || (c.indexOf(V) != -1 || m.external && m.external.gwtOnLoad)) && c.indexOf(W) == -1
        } catch (a) {}
        B = function() {
            return b
        }
        ;
        return b
    }
    function C() {
        if (q && r) {
            var b = n.getElementById(Q);
            var c = b.contentWindow;
            if (B()) {
                c.__gwt_getProperty = function(a) {
                    return H(a)
                }
            }
            webbraingwt = null;
            c.gwtOnLoad(z, Q, t, y);
            o && o({
                moduleName: Q,
                sessionId: p,
                subSystem: R,
                evtGroup: X,
                millis: (new Date).getTime(),
                type: Y
            })
        }
    }
    function D() {
        function e(a) {
            var b = a.lastIndexOf(Z);
            if (b == -1) {
                b = a.length
            }
            var c = a.indexOf($);
            if (c == -1) {
                c = a.length
            }
            var d = a.lastIndexOf(_, Math.min(c, b));
            return d >= 0 ? a.substring(0, d + 1) : P
        }
        function f(a) {
            if (a.match(/^\w+:\/\//)) {} else {
                var b = n.createElement(ab);
                b.src = a + bb;
                a = e(b.src)
            }
            return a
        }
        function g() {
            var a = F(cb);
            if (a != null) {
                return a
            }
            return P
        }
        function h() {
            var a = n.getElementsByTagName(db);
            for (var b = 0; b < a.length; ++b) {
                if (a[b].src.indexOf(eb) != -1) {
                    return e(a[b].src)
                }
            }
            return P
        }
        function i() {
            var a;
            if (typeof isBodyLoaded == fb || !isBodyLoaded()) {
                var b = gb;
                var c;
                n.write(hb + b + ib);
                c = n.getElementById(b);
                a = c && c.previousSibling;
                while (a && a.tagName != jb) {
                    a = a.previousSibling
                }
                if (c) {
                    c.parentNode.removeChild(c)
                }
                if (a && a.src) {
                    return e(a.src)
                }
            }
            return P
        }
        function j() {
            var a = n.getElementsByTagName(kb);
            if (a.length > 0) {
                return a[a.length - 1].href
            }
            return P
        }
        function k() {
            var a = n.location;
            return a.href == a.protocol + lb + a.host + a.pathname + a.search + a.hash
        }
        var l = g();
        if (l == P) {
            l = h()
        }
        if (l == P) {
            l = i()
        }
        if (l == P) {
            l = j()
        }
        if (l == P && k()) {
            l = e(n.location.href)
        }
        l = f(l);
        t = l;
        return l
    }
    function E() {
        var b = document.getElementsByTagName(mb);
        for (var c = 0, d = b.length; c < d; ++c) {
            var e = b[c], f = e.getAttribute(nb), g;
            if (f) {
                f = f.replace(ob, P);
                if (f.indexOf(pb) >= 0) {
                    continue
                }
                if (f == qb) {
                    g = e.getAttribute(rb);
                    if (g) {
                        var h, i = g.indexOf(sb);
                        if (i >= 0) {
                            f = g.substring(0, i);
                            h = g.substring(i + 1)
                        } else {
                            f = g;
                            h = P
                        }
                        u[f] = h
                    }
                } else if (f == tb) {
                    g = e.getAttribute(rb);
                    if (g) {
                        try {
                            A = eval(g)
                        } catch (a) {
                            alert(ub + g + vb)
                        }
                    }
                } else if (f == wb) {
                    g = e.getAttribute(rb);
                    if (g) {
                        try {
                            z = eval(g)
                        } catch (a) {
                            alert(ub + g + xb)
                        }
                    }
                }
            }
        }
    }
    function F(a) {
        var b = u[a];
        return b == null ? null : b
    }
    function G(a, b) {
        var c = x;
        for (var d = 0, e = a.length - 1; d < e; ++d) {
            c = c[a[d]] || (c[a[d]] = [])
        }
        c[a[e]] = b
    }
    function H(a) {
        var b = w[a]()
          , c = v[a];
        if (b in c) {
            return b
        }
        var d = [];
        for (var e in c) {
            d[c[e]] = e
        }
        if (A) {
            A(a, d, b)
        }
        throw null
    }
    var I;
    function J() {
        if (!I) {
            I = true;
            var a = n.createElement(yb);
            a.src = zb;
            a.id = Q;
            a.style.cssText = Ab;
            a.tabIndex = -1;
            n.body.appendChild(a);
            o && o({
                moduleName: Q,
                sessionId: p,
                subSystem: R,
                evtGroup: X,
                millis: (new Date).getTime(),
                type: Bb
            });
            a.contentWindow.location.replace(t + L)
        }
    }
    w[Cb] = function() {
        var a = navigator.userAgent.toLowerCase();
        if (a.indexOf(Db) != -1 || a.indexOf(Eb) != -1) {
            return Db
        } else if (a.indexOf(Fb) != -1) {
            return Fb
        } else if (a.indexOf(Gb) != -1) {
            if (a.indexOf(Hb) != -1) {
                return Ib
            } else if (a.indexOf(Jb) != -1) {
                return Ib
            } else {
                return Gb
            }
        } else if (a.indexOf(Kb) != -1) {
            return Ib
        }
        return Lb
    }
    ;
    v[Cb] = {
        android: 0,
        androidMobile: 1,
        browser: 2,
        embeddedAndroid: 3,
        embeddedIOS: 4,
        ipad: 5,
        iphone: 6
    };
    w[Mb] = function() {
        if (!!m.WebKitCSSMatrix) {
            var a = (new WebKitCSSMatrix).translate(1, 0, 0);
            var b = (new WebKitCSSMatrix).scale(5, 1, 1);
            if (b.multiply(a).m41 > a.multiply(b).m41) {
                return Nb
            } else {
                return Ob
            }
        }
        return Nb
    }
    ;
    v[Mb] = {
        column_major: 0,
        row_major: 1
    };
    w[Pb] = function() {
        var b = navigator.userAgent.toLowerCase();
        var c = function(a) {
            return parseInt(a[1]) * 1000 + parseInt(a[2])
        };
        if (function() {
            return b.indexOf(Qb) != -1
        }())
            return Qb;
        if (function() {
            return b.indexOf(Rb) != -1
        }())
            return Sb;
        if (function() {
            return b.indexOf(Tb) != -1 && n.documentMode >= 9
        }())
            return Ub;
        if (function() {
            return b.indexOf(Tb) != -1 && n.documentMode >= 8
        }())
            return Vb;
        if (function() {
            var a = /msie ([0-9]+)\.([0-9]+)/.exec(b);
            if (a && a.length == 3)
                return c(a) >= 6000
        }())
            return Wb;
        if (function() {
            return b.indexOf(Xb) != -1
        }())
            return Yb;
        return Zb
    }
    ;
    v[Pb] = {
        gecko1_8: 0,
        ie6: 1,
        ie8: 2,
        ie9: 3,
        opera: 4,
        safari: 5
    };
    webbraingwt.onScriptLoad = function() {
        if (I) {
            r = true;
            C()
        }
    }
    ;
    webbraingwt.onInjectionDone = function() {
        q = true;
        o && o({
            moduleName: Q,
            sessionId: p,
            subSystem: R,
            evtGroup: $b,
            millis: (new Date).getTime(),
            type: Y
        });
        C()
    }
    ;
    E();
    D();
    var K;
    var L;
    if (B()) {
        if (m.external && (m.external.initModule && m.external.initModule(Q))) {
            m.location.reload();
            return
        }
        L = _b;
        K = P
    }
    o && o({
        moduleName: Q,
        sessionId: p,
        subSystem: R,
        evtGroup: S,
        millis: (new Date).getTime(),
        type: ac
    });
    if (!B()) {
        try {
            G([Db, Ob, Sb], bc);
            G([Db, Nb, Sb], cc);
            G([Lb, Nb, Yb], dc);
            G([Lb, Nb, Qb], ec);
            G([Lb, Ob, Sb], fc);
            G([gc, Ob, Sb], fc);
            G([hc, Ob, Sb], fc);
            G([Lb, Ob, Sb], fc + ic);
            G([gc, Ob, Sb], fc + ic);
            G([hc, Ob, Sb], fc + ic);
            G([Lb, Ob, Sb], fc + jc);
            G([gc, Ob, Sb], fc + jc);
            G([hc, Ob, Sb], fc + jc);
            G([Ib, Ob, Sb], kc);
            G([Lb, Nb, Wb], lc);
            G([Ib, Nb, Sb], mc);
            G([Gb, Ob, Sb], nc);
            G([Gb, Nb, Sb], oc);
            G([Lb, Nb, Ub], pc);
            G([Lb, Nb, Vb], qc);
            G([Fb, Ob, Sb], rc);
            G([Fb, Nb, Sb], sc);
            G([Lb, Nb, Sb], tc);
            G([gc, Nb, Sb], tc);
            G([hc, Nb, Sb], tc);
            G([Lb, Nb, Sb], tc + ic);
            G([gc, Nb, Sb], tc + ic);
            G([hc, Nb, Sb], tc + ic);
            G([Lb, Nb, Sb], tc + jc);
            G([gc, Nb, Sb], tc + jc);
            G([hc, Nb, Sb], tc + jc);
            K = x[H(Cb)][H(Mb)][H(Pb)];
            var M = K.indexOf(uc);
            if (M != -1) {
                y = Number(K.substring(M + 1));
                K = K.substring(0, M)
            }
            L = K + vc
        } catch (a) {
            return
        }
    }
    var N;
    function O() {
        if (!s) {
            s = true;
            C();
            if (n.removeEventListener) {
                n.removeEventListener(wc, O, false)
            }
            if (N) {
                clearInterval(N)
            }
        }
    }
    if (n.addEventListener) {
        n.addEventListener(wc, function() {
            J();
            O()
        }, false)
    }
    var N = setInterval(function() {
        if (/loaded|complete/.test(n.readyState)) {
            J();
            O()
        }
    }, 50);
    o && o({
        moduleName: Q,
        sessionId: p,
        subSystem: R,
        evtGroup: S,
        millis: (new Date).getTime(),
        type: Y
    });
    o && o({
        moduleName: Q,
        sessionId: p,
        subSystem: R,
        evtGroup: $b,
        millis: (new Date).getTime(),
        type: T
    });
    n.write(xc)
}
webbraingwt();
