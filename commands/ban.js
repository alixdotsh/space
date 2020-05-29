module.exports = message => {
	const user = message.mentions.users.first();
	if (user) {
		const member = message.guild.member(user);
		if (member) {
			member
				.ban({
					reason: `Banned by Nurple`
				})
				.then(() => {
					message.reply(`I have used the ban hammer on ${user.tag}!`);
				})
				.catch(err => {
					// If the error happens, most likely because they do not have the permission to kick or they are missing permissions
					message.reply(`I was not able to use the ban hammer!`);
					console.error(err);
				});
		} else {
			//The user is not in the guild
			message.reply("That user does not exist in this guild!")
		}
	} else {
		//Otherwise, no user was mentioned
		message.reply("You did not tell me who to use the ban hammer on!")
	}
}
