const downword = document.getElementById('up')
const upword = document.querySelector('.down')
const main = document.querySelector('aside')
downword.addEventListener('click', e => {
    e.preventDefault()
    main.scrollTo(0, main.scrollHeight)
})
upword.addEventListener('click', e => {
    e.preventDefault()
    main.scrollTo(0, 0)
})