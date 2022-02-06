import React from 'react';

function ProductLoading(Component) {
    return function ProductLoadingComponent({ isLoading, ...props}) {
        if (!isLoading) return <Component {...props} />;
        return (
            <p style={{ fontSize:'25px'}}>
                로그인 후 이용해주세요.
            </p>
        );
    };
}
export default ProductLoading;