export const loginRequired = async (req, res, next) => {
    let token = req.headers['authorization']
    if (!token) return res.status(401).json({error: 'An access token is required to proceed'});
    try {
        token = token.split(' ')[1];
    } catch (error) {
        return res.status(401).json({error: 'Invalid access token'});
    }
    next();
}