import {useCallback, useState} from "react";

export default function useArray<E>(initialArray: E[] = []) {
    const [array, setArray] = useState<E[]>(initialArray);

    const add = useCallback((e: E) => {
        setArray([...array, e]);
    }, [array]);

    const remove = useCallback((e: E) => {
        setArray(array.filter(a => a !== e));
    }, [array]);

    return [array, add, remove] as [E[], typeof add, typeof remove];
}
