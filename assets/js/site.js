(function(){
  var sets=window.WN_SETS||[];
  var d=document.getElementById('view'),img=document.getElementById('vimg'),i=0,opener=null;
  var vtxt=document.getElementById('vtxt'),vlink=document.getElementById('vlink');
  function show(n){i=(n+sets.length)%sets.length;var s=sets[i];img.src=s.s;img.alt=s.a;vtxt.textContent=s.c;vlink.href=s.p}
  function open(b){opener=b;show(+b.dataset.i);if(d.showModal)d.showModal();else d.setAttribute('open','')}
  function close(){if(d.close)d.close();else d.removeAttribute('open');if(opener&&opener.focus)opener.focus()}
  [].forEach.call(document.querySelectorAll('.print'),function(b){b.addEventListener('click',function(){open(b)})});
  document.getElementById('x').onclick=close;
  document.getElementById('prev').onclick=function(){show(i-1)};
  document.getElementById('next').onclick=function(){show(i+1)};
  document.addEventListener('keydown',function(e){if(!d.open)return;if(e.key==='ArrowLeft'){e.preventDefault();show(i-1)}if(e.key==='ArrowRight'){e.preventDefault();show(i+1)}});
  d.addEventListener('cancel',function(){setTimeout(function(){if(opener&&opener.focus)opener.focus()},0)});
  d.addEventListener('click',function(e){if(e.target===d)close()});
  var sx=0;d.addEventListener('touchstart',function(e){sx=e.touches[0].clientX},{passive:true});
  d.addEventListener('touchend',function(e){var dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>50)show(i+(dx<0?1:-1))},{passive:true});
  // later prints fade up once as they enter (only styled hidden when motion is allowed)
  var f=[].slice.call(document.querySelectorAll('.fade'));
  function reveal(){f.forEach(function(x){x.classList.add('in')})}
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});f.forEach(function(x){io.observe(x)});
    addEventListener('hashchange',reveal);addEventListener('beforeprint',reveal);
    if(location.hash)reveal();
  }else reveal();
})();
