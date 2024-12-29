function checkInclusion(s1: string, s2: string): boolean {
	const desiredMap = s1
		.split('')
		.reduce<Record<string, number>>((acc, curr) => {
			acc[curr] ??= 0;
			acc[curr] += 1;

			return acc;
		}, {});

	let leftP = 0;
	let rightP = s1.length - 1;

	outer: while (rightP <= s1.length - 1) {
		const map = {};

		for (let i = leftP; i < rightP; i += 1) {
			if (!desiredMap[s2[i]]) {
				break;
			}

			map[s2[i]] ??= 0;
			acc[s2[i]] = +1;
		}

		leftP += 1;
		rightP += 1;

		for (let key in map) {
			if (desiredMap[key] !== map[key]) {
				break;
				continue outer;
			}
		}

		return true;
	}

	return false;
}
