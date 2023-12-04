import jwt from 'jsonwebtoken';

export const loginRequired = (req, res, next) => {
    let token = req.headers['authorization']
    if (!token) return res.status(401).json({message: 'An access token is required to proceed'});
    token = token.split(' ')[1];
    console.log(token, process.env.JWT_SECRET);
    jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
        if (err) {
            return res.status(403).json({ message: 'Forbidden - Invalid token' });
        }

        console.log("User authenticated");

        req.user = user;
        console.log("User", user);
        next();
    });
}