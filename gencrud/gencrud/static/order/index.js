const claimModalFormComponent = ClaimModalFormComponent(_userId, _userEmail, _userPhone);
const productClaimModalFormComponent = ProductClaimModalFormComponent(_userId, _userEmail, _userPhone);

const claimFormModal = new ClaimFormModal(claimModalFormComponent);
const productClaimForm = new ProductClaimForm(productClaimModalFormComponent);
const productItemsClaimForm = new ProductItemsClaimForm(productClaimModalFormComponent);

claimFormModal.init();
productClaimForm.init();
productItemsClaimForm.init();
