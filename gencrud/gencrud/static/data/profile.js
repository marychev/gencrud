function getHiddenProfileData() {
    const hidden = document.getElementById('profileData');
    return {
        id: hidden.dataset.userId,
        email: hidden.dataset.userEmail,
        phone: hidden.dataset.profilePhone,
    }
}

const profileData = getHiddenProfileData();
const _userId = profileData.id;
const _userEmail = profileData.email;
const _userPhone = profileData.phone;