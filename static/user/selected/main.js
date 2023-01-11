const next = document.querySelectorAll('.next');
const prev = document.querySelectorAll('.prev');
const slider = document.querySelectorAll('.slider')

for(let i =0;i<slider.length;i++){
    getMovies(slider[i],i+1);
    makeSlider(slider[i],prev[i],next[i]);
}
function makeSlidr(element,prev,next){
    next.addEventListener('click',()=>{
        const offsetX = element.offsetWidth;
        element.scrollBy(offsetX,0)
    })
    prev.addEventListener('click',()=>{
        const offsetX = element.offsetWidth;
        element.scrollBy(-offsetX,0)
    })
}
function getMoviese(element,page){
    // fetch(`https://yts.mx/api/v2/list_movies.json?limit=20&sort_by=rating&page=${page}`)
    //     .then(data=>data.json())
    //     .then(data=>{
    //         const movies = data.data.movies;
    //         movies.forEach(movie=>{
    //             const div = document.createElement('div');
    //             div.className='item';
    //             div.innerHTML = `<img src="${movie.medium_cover_image}" alt="">`;
    //             element.appendChild(div);
    //         })
    //     })
}
