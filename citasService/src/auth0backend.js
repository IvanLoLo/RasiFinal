import axios from 'axios'

const getRole = async (req) => {
    const accessToken = req.headers.authorization.split(' ')[1];
    if (!accessToken) return 'Unauthorized';
    try {
        const user = await axios.get(`https://${process.env.DOMAIN}/userinfo`, {
            headers: {
                'Authorization': 'Bearer ' + accessToken
            }
        });
        return user['data']['roles/'][0];
    } catch (error) {
        console.log(error);
        return 'Unauthorized';
    }
}

export default getRole;