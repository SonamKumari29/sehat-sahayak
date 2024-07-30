let next = document.querySelector('.next');
let prev = document.querySelector('.prev');


next.addEventListener('click', function() {
   let items=document.querySelectorAll(".items")
   document.querySelector(".slides").appendChild(items[0])
})

prev.addEventListener('click', function() {
    let items=document.querySelectorAll(".items")
   document.querySelector(".slides").prepend(items[items.length-1]);
});
