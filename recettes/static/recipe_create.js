const addIngredientButton = document.querySelector('#add-ingredient-button');
const ingredientList = document.querySelector('#ingredient-list');
const newIngredientInput = document.querySelector('#new-ingredient-input');

addIngredientButton.addEventListener('click', () => {
  const newIngredient = newIngredientInput.value.trim();
  if (newIngredient !== '') {
    const listItem = document.createElement('li');
    listItem.textContent = newIngredient;
    ingredientList.appendChild(listItem);
    newIngredientInput.value = '';
  }
});