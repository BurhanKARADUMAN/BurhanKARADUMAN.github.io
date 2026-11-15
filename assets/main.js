(function(){
 const menu=document.querySelector('.menu-toggle');
 const nav=document.getElementById('primary-nav');
 if(menu && nav){menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Close navigation':'Open navigation');nav.classList.toggle('show',open)});nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('show');menu.setAttribute('aria-expanded','false')}));}
 const filters=[...document.querySelectorAll('[data-filter]')];const cards=[...document.querySelectorAll('.project-card')];const status=document.getElementById('visible-projects');
 filters.forEach(button=>button.addEventListener('click',()=>{const selected=button.dataset.filter;filters.forEach(b=>{const active=b===button;b.classList.toggle('active',active);b.setAttribute('aria-pressed',String(active))});let shown=0;cards.forEach(card=>{const visible=selected==='all'||card.dataset.category.split(' ').includes(selected);card.hidden=!visible;if(visible)shown++});if(status)status.textContent='Showing '+shown+' of '+cards.length+' projects'}));
})();
