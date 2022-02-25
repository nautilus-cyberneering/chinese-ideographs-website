var app=function(){"use strict";function t(){}function e(t){return t()}function n(){return Object.create(null)}function o(t){t.forEach(e)}function r(t){return"function"==typeof t}function l(t,e){return t!=t?e==e:t!==e||t&&"object"==typeof t||"function"==typeof t}let i,s;function c(t,e){return i||(i=document.createElement("a")),i.href=e,t===i.href}function a(t,e){t.appendChild(e)}function f(t,e,n){t.insertBefore(e,n||null)}function u(t){t.parentNode.removeChild(t)}function d(t){return document.createElement(t)}function g(t){return document.createTextNode(t)}function p(){return g(" ")}function m(t,e,n){null==n?t.removeAttribute(e):t.getAttribute(e)!==n&&t.setAttribute(e,n)}function h(t){s=t}const $=[],b=[],_=[],y=[],x=Promise.resolve();let v=!1;function j(t){_.push(t)}let k=!1;const w=new Set;function E(){if(!k){k=!0;do{for(let t=0;t<$.length;t+=1){const e=$[t];h(e),C(e.$$)}for(h(null),$.length=0;b.length;)b.pop()();for(let t=0;t<_.length;t+=1){const e=_[t];w.has(e)||(w.add(e),e())}_.length=0}while($.length);for(;y.length;)y.pop()();v=!1,k=!1,w.clear()}}function C(t){if(null!==t.fragment){t.update(),o(t.before_update);const e=t.dirty;t.dirty=[-1],t.fragment&&t.fragment.p(t.ctx,e),t.after_update.forEach(j)}}const N=new Set;function A(t,e){-1===t.$$.dirty[0]&&($.push(t),v||(v=!0,x.then(E)),t.$$.dirty.fill(0)),t.$$.dirty[e/31|0]|=1<<e%31}function O(l,i,c,a,f,d,g,p=[-1]){const m=s;h(l);const $=l.$$={fragment:null,ctx:null,props:d,update:t,not_equal:f,bound:n(),on_mount:[],on_destroy:[],on_disconnect:[],before_update:[],after_update:[],context:new Map(m?m.$$.context:i.context||[]),callbacks:n(),dirty:p,skip_bound:!1,root:i.target||m.$$.root};g&&g($.root);let b=!1;if($.ctx=c?c(l,i.props||{},((t,e,...n)=>{const o=n.length?n[0]:e;return $.ctx&&f($.ctx[t],$.ctx[t]=o)&&(!$.skip_bound&&$.bound[t]&&$.bound[t](o),b&&A(l,t)),e})):[],$.update(),b=!0,o($.before_update),$.fragment=!!a&&a($.ctx),i.target){if(i.hydrate){const t=function(t){return Array.from(t.childNodes)}(i.target);$.fragment&&$.fragment.l(t),t.forEach(u)}else $.fragment&&$.fragment.c();i.intro&&((_=l.$$.fragment)&&_.i&&(N.delete(_),_.i(y))),function(t,n,l,i){const{fragment:s,on_mount:c,on_destroy:a,after_update:f}=t.$$;s&&s.m(n,l),i||j((()=>{const n=c.map(e).filter(r);a?a.push(...n):o(n),t.$$.on_mount=[]})),f.forEach(j)}(l,i.target,i.anchor,i.customElement),E()}var _,y;h(m)}function S(t,e,n){const o=t.slice();return o[1]=e[n].id,o[2]=e[n].filename,o[4]=n,o}function B(t){let e,n,o,r,l,i,s,h,$,b,_=t[2]+"";return{c(){e=d("div"),n=d("a"),o=d("img"),i=p(),s=d("span"),h=g(_),b=p(),c(o.src,r="./images/"+t[2])||m(o,"src",r),m(o,"alt",l=t[2]),m(o,"class","svelte-63agpb"),m(s,"class","svelte-63agpb"),m(n,"target","_blank"),m(n,"href",$="./images/"+t[2]),m(n,"class","svelte-63agpb"),m(e,"class","item svelte-63agpb")},m(t,r){f(t,e,r),a(e,n),a(n,o),a(n,i),a(n,s),a(s,h),a(e,b)},p(t,e){1&e&&!c(o.src,r="./images/"+t[2])&&m(o,"src",r),1&e&&l!==(l=t[2])&&m(o,"alt",l),1&e&&_!==(_=t[2]+"")&&function(t,e){e=""+e,t.wholeText!==e&&(t.data=e)}(h,_),1&e&&$!==($="./images/"+t[2])&&m(n,"href",$)},d(t){t&&u(e)}}}function T(t){let e,n=t[2].endsWith(".jpg"),o=n&&B(t);return{c(){o&&o.c(),e=g("")},m(t,n){o&&o.m(t,n),f(t,e,n)},p(t,r){1&r&&(n=t[2].endsWith(".jpg")),n?o?o.p(t,r):(o=B(t),o.c(),o.m(e.parentNode,e)):o&&(o.d(1),o=null)},d(t){o&&o.d(t),t&&u(e)}}}function W(e){let n,o,r,l,i,s,c=e[0],g=[];for(let t=0;t<c.length;t+=1)g[t]=T(S(e,c,t));return{c(){n=d("main"),o=d("h1"),o.textContent="Chinese Ideographs",r=p(),l=d("h2"),l.textContent="Base Drawings",i=p(),s=d("div");for(let t=0;t<g.length;t+=1)g[t].c();m(o,"class","svelte-63agpb"),m(l,"class","svelte-63agpb"),m(s,"class","gallery svelte-63agpb"),m(n,"class","svelte-63agpb")},m(t,e){f(t,n,e),a(n,o),a(n,r),a(n,l),a(n,i),a(n,s);for(let t=0;t<g.length;t+=1)g[t].m(s,null)},p(t,[e]){if(1&e){let n;for(c=t[0],n=0;n<c.length;n+=1){const o=S(t,c,n);g[n]?g[n].p(o,e):(g[n]=T(o),g[n].c(),g[n].m(s,null))}for(;n<g.length;n+=1)g[n].d(1);g.length=c.length}},i:t,o:t,d(t){t&&u(n),function(t,e){for(let n=0;n<t.length;n+=1)t[n]&&t[n].d(e)}(g,t)}}}function q(t,e,n){let{image_files:o=[]}=e;return console.log(o),t.$$set=t=>{"image_files"in t&&n(0,o=t.image_files)},[o]}return new class extends class{$destroy(){!function(t,e){const n=t.$$;null!==n.fragment&&(o(n.on_destroy),n.fragment&&n.fragment.d(e),n.on_destroy=n.fragment=null,n.ctx=[])}(this,1),this.$destroy=t}$on(t,e){const n=this.$$.callbacks[t]||(this.$$.callbacks[t]=[]);return n.push(e),()=>{const t=n.indexOf(e);-1!==t&&n.splice(t,1)}}$set(t){var e;this.$$set&&(e=t,0!==Object.keys(e).length)&&(this.$$.skip_bound=!0,this.$$set(t),this.$$.skip_bound=!1)}}{constructor(t){super(),O(this,t,q,W,l,{image_files:0})}}({target:document.body,props:{image_files:JSON.parse('[{"id":1,"filename":"000000-42.600.2.jpg"},{"id":2,"filename":"000001-42.600.2.jpg"},{"id":3,"filename":"000002-42.600.2.jpg"},{"id":4,"filename":"000003-42.600.2.jpg"},{"id":5,"filename":"000004-42.600.2.jpg"},{"id":6,"filename":"000005-42.600.2.jpg"},{"id":7,"filename":"000006-42.600.2.jpg"},{"id":8,"filename":"000007-42.600.2.jpg"}]')}})}();
//# sourceMappingURL=bundle.js.map
