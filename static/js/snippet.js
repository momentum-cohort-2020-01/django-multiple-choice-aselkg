function myFunction () {
  var input, filter, ul, li, a, i, desc, lang, txtValue
  input = document.getElementById('searchBar')
  filter = input.value.toUpperCase()
  ul = document.getElementById('snippetList')
  li = ul.getElementsByTagName('li')
  desc = document.getElementsByClassName('code-body')
  lang = document.getElementsByClassName('code-lang')
  for (i = 0; i < li.length; i++) {
    a = li[i].getElementsByTagName('a')[0]
    txtValue = a.textContent || a.innerText
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = ''
    } else {
      li[i].style.display = 'none'
    }
  }
}
function copyToClipboard (element) {
  var $temp = $('<input>')
  $('body').append($temp)
  $temp.val($(element).text()).select()
  document.execCommand('copy')
  $temp.remove()
}
