// HttpSessionDirector = session.setAttribue('sessiondirector', selected_director);

// window.sessionStorage = window.sessionStorage || (function () {
//     let winObj = openr || window;
//     let data = JSON.parse(winObj.top.name || '{}');

//     let fn = {
//         length : Object.keys(data).length,
//         setItem : function(key, value) {
//             data[key] = value + '';
//             winObj.top.name = JSON.stringify(data);
//             fn.length++;
//         },
//         getItem : function(key) {
//             return data[key] || null;
//         },
//         key : function(idx) {
//             return Object.keys(data)[idx] || null;
//         },
//         removeItem : function(key) {
//             delete data[key];
//             winObj.top.name = JSON.stringify(data);
//             fn.length--;
//         },
//         clear : function() {
//             winObj.top.name = '{}';
//             fn.length = 0;
//         }
//     };
//     return fn;
// })();

// // function selectedDirectorSession() {
// //     selected_director = document.getElementById("selected_director").value;
// //     sStorage.setItem("sdirector", selected_director);
// // }

// selected_director = document.getElementById("selected_director").value;
// sStorage.setItem("sdirector", selected_director);
// // sStorage.setItem("key2", new Date());
// console.log(sStorage.getItem("sdirector"));
// // console.log(sStorage.getItem("key2"));
// // sStorage.removeItem('key2');
// // sStorage.setItem("key3", '새 문자');
// // console.log(sStorage.length);   
// // console.log(sStorage.key(1));
// // sStorage.clear();
// // console.log(sStorage.length);

// sessionStorage.setItem('selected_director',JSON.stringify(selected_director));
// sessionStorage.setItem("selected_director",JSON.stringify(selected_director));

    
function sessionDataImport() {
    let selected_director = document.getElementById("selected_director").value;
    sessionStorage.setItem("selected_director",selected_director);
    // sessionStorage.getItem("selected_director");
    
}
// function sessionDataExport() {
    // sessionStorage.getItem("selected_director");
// }



