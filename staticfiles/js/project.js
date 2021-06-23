document.addEventListener('DOMContentLoaded', ()=>{
    $('.carousel').carousel({
        interval: 2000,
      })

    const link = document.getElementById('nav2-ul-li-menu')
    link.addEventListener('click', function(){
        const di = document.getElementById('menu-div');
        di.classList.toggle('hidden');
        di.classList.toggle('inline-b');
    })
        
})


