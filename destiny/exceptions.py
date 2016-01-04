class TransportException(Exception):
    pass
class UnhandledException(Exception):
    pass
class NotImplemented(Exception):
    pass
class SystemDisabled(Exception):
    pass
class FailedToLoadAvailableLocalesConfiguration(Exception):
    pass
class ParameterParseFailure(Exception):
    pass
class ParameterInvalidRange(Exception):
    pass
class BadRequest(Exception):
    pass
class AuthenticationInvalid(Exception):
    pass
class DataNotFound(Exception):
    pass
class InsufficientPrivileges(Exception):
    pass
class Duplicate(Exception):
    pass
class UnknownSqlResult(Exception):
    pass
class ValidationError(Exception):
    pass
class ValidationMissingFieldError(Exception):
    pass
class ValidationInvalidInputError(Exception):
    pass
class InvalidParameters(Exception):
    pass
class ParameterNotFound(Exception):
    pass
class UnhandledHttpException(Exception):
    pass
class NotFound(Exception):
    pass
class WebAuthModuleAsyncFailed(Exception):
    pass
class InvalidReturnValue(Exception):
    pass
class UserBanned(Exception):
    pass
class InvalidPostBody(Exception):
    pass
class MissingPostBody(Exception):
    pass
class ExternalServiceTimeout(Exception):
    pass
class ValidationLengthError(Exception):
    pass
class ValidationRangeError(Exception):
    pass
class JsonDeserializationError(Exception):
    pass
class ThrottleLimitExceeded(Exception):
    pass
class ValidationTagError(Exception):
    pass
class ValidationProfanityError(Exception):
    pass
class ValidationUrlFormatError(Exception):
    pass
class ThrottleLimitExceededMinutes(Exception):
    pass
class ThrottleLimitExceededMomentarily(Exception):
    pass
class ThrottleLimitExceededSeconds(Exception):
    pass
class ExternalServiceUnknown(Exception):
    pass
class ValidationWordLengthError(Exception):
    pass
class ValidationInvisibleUnicode(Exception):
    pass
class ValidationBadNames(Exception):
    pass
class ExternalServiceFailed(Exception):
    pass
class ServiceRetired(Exception):
    pass
class UnknownSqlException(Exception):
    pass
class UnsupportedLocale(Exception):
    pass
class InvalidPageNumber(Exception):
    pass
class MaximumPageSizeExceeded(Exception):
    pass
class ServiceUnsupported(Exception):
    pass
class ValidationMaximumUnicodeCombiningCharacters(Exception):
    pass
class UnableToUnPairMobileApp(Exception):
    pass
class UnableToPairMobileApp(Exception):
    pass
class CannotUseMobileAuthWithNonMobileProvider(Exception):
    pass
class MissingDeviceCookie(Exception):
    pass
class FacebookTokenExpired(Exception):
    pass
class AuthTicketRequired(Exception):
    pass
class CookieContextRequired(Exception):
    pass
class UnknownAuthenticationError(Exception):
    pass
class BungieNetAccountCreationRequired(Exception):
    pass
class WebAuthRequired(Exception):
    pass
class ContentUnknownSqlResult(Exception):
    pass
class ContentNeedUniquePath(Exception):
    pass
class ContentSqlException(Exception):
    pass
class ContentNotFound(Exception):
    pass
class ContentSuccessWithTagAddFail(Exception):
    pass
class ContentSearchMissingParameters(Exception):
    pass
class ContentInvalidId(Exception):
    pass
class ContentPhysicalFileDeletionError(Exception):
    pass
class ContentPhysicalFileCreationError(Exception):
    pass
class ContentPerforceSubmissionError(Exception):
    pass
class ContentPerforceInitializationError(Exception):
    pass
class ContentDeploymentPackageNotReadyError(Exception):
    pass
class ContentUploadFailed(Exception):
    pass
class ContentTooManyResults(Exception):
    pass
class ContentInvalidState(Exception):
    pass
class ContentNavigationParentNotFound(Exception):
    pass
class ContentNavigationParentUpdateError(Exception):
    pass
class DeploymentPackageNotEditable(Exception):
    pass
class ContentValidationError(Exception):
    pass
class ContentPropertiesValidationError(Exception):
    pass
class ContentTypeNotFound(Exception):
    pass
class DeploymentPackageNotFound(Exception):
    pass
class ContentSearchInvalidParameters(Exception):
    pass
class ContentItemPropertyAggregationError(Exception):
    pass
class DeploymentPackageFileNotFound(Exception):
    pass
class ContentPerforceFileHistoryNotFound(Exception):
    pass
class ContentAssetZipCreationFailure(Exception):
    pass
class ContentAssetZipCreationBusy(Exception):
    pass
class ContentProjectNotFound(Exception):
    pass
class ContentFolderNotFound(Exception):
    pass
class ContentPackagesInconsistent(Exception):
    pass
class ContentPackagesInvalidState(Exception):
    pass
class ContentPackagesInconsistentType(Exception):
    pass
class ContentCannotDeletePackage(Exception):
    pass
class ContentLockedForChanges(Exception):
    pass
class ContentFileUploadFailed(Exception):
    pass
class ContentNotReviewed(Exception):
    pass
class ContentPermissionDenied(Exception):
    pass
class ContentInvalidExternalUrl(Exception):
    pass
class ContentExternalFileCannotBeImportedLocally(Exception):
    pass
class ContentTagSaveFailure(Exception):
    pass
class ContentPerforceUnmatchedFileError(Exception):
    pass
class ContentPerforceChangelistResultNotFound(Exception):
    pass
class ContentPerforceChangelistFileItemsNotFound(Exception):
    pass
class ContentPerforceInvalidRevisionError(Exception):
    pass
class ContentUnloadedSaveResult(Exception):
    pass
class ContentPropertyInvalidNumber(Exception):
    pass
class ContentPropertyInvalidUrl(Exception):
    pass
class ContentPropertyInvalidDate(Exception):
    pass
class ContentPropertyInvalidSet(Exception):
    pass
class ContentPropertyCannotDeserialize(Exception):
    pass
class ContentRegexValidationFailOnProperty(Exception):
    pass
class ContentMaxLengthFailOnProperty(Exception):
    pass
class ContentPropertyUnexpectedDeserializationError(Exception):
    pass
class ContentPropertyRequired(Exception):
    pass
class ContentCannotCreateFile(Exception):
    pass
class ContentInvalidMigrationFile(Exception):
    pass
class ContentMigrationAlteringProcessedItem(Exception):
    pass
class ContentPropertyDefinitionNotFound(Exception):
    pass
class ContentReviewDataChanged(Exception):
    pass
class ContentRollbackRevisionNotInPackage(Exception):
    pass
class ContentItemNotBasedOnLatestRevision(Exception):
    pass
class ContentUnauthorized(Exception):
    pass
class ContentCannotCreateDeploymentPackage(Exception):
    pass
class ContentUserNotFound(Exception):
    pass
class ContentLocalePermissionDenied(Exception):
    pass
class ContentInvalidLinkToInternalEnvironment(Exception):
    pass
class ContentInvalidBlacklistedContent(Exception):
    pass
class UserNonUniqueName(Exception):
    pass
class UserManualLinkingStepRequired(Exception):
    pass
class UserCreateUnknownSqlResult(Exception):
    pass
class UserCreateUnknownSqlException(Exception):
    pass
class UserMalformedMembershipId(Exception):
    pass
class UserCannotFindRequestedUser(Exception):
    pass
class UserCannotLoadAccountCredentialLinkInfo(Exception):
    pass
class UserInvalidMobileAppType(Exception):
    pass
class UserMissingMobilePairingInfo(Exception):
    pass
class UserCannotGenerateMobileKeyWhileUsingMobileCredential(Exception):
    pass
class UserGenerateMobileKeyExistingSlotCollision(Exception):
    pass
class UserDisplayNameMissingOrInvalid(Exception):
    pass
class UserCannotLoadAccountProfileData(Exception):
    pass
class UserCannotSaveUserProfileData(Exception):
    pass
class UserEmailMissingOrInvalid(Exception):
    pass
class UserTermsOfUseRequired(Exception):
    pass
class UserCannotCreateNewAccountWhileLoggedIn(Exception):
    pass
class UserCannotResolveCentralAccount(Exception):
    pass
class UserInvalidAvatar(Exception):
    pass
class UserMissingCreatedUserResult(Exception):
    pass
class UserCannotChangeUniqueNameYet(Exception):
    pass
class UserCannotChangeDisplayNameYet(Exception):
    pass
class UserCannotChangeEmail(Exception):
    pass
class UserUniqueNameMustStartWithLetter(Exception):
    pass
class UserNoLinkedAccountsSupportFriendListings(Exception):
    pass
class UserAcknowledgmentTableFull(Exception):
    pass
class MessagingUnknownError(Exception):
    pass
class MessagingSelfError(Exception):
    pass
class MessagingSendThrottle(Exception):
    pass
class MessagingNoBody(Exception):
    pass
class MessagingTooManyUsers(Exception):
    pass
class MessagingCanNotLeaveConversation(Exception):
    pass
class MessagingUnableToSend(Exception):
    pass
class MessagingDeletedUserForbidden(Exception):
    pass
class MessagingCannotDeleteExternalConversation(Exception):
    pass
class MessagingGroupChatDisabled(Exception):
    pass
class MessagingMustIncludeSelfInPrivateMessage(Exception):
    pass
class AddSurveyAnswersUnknownSqlException(Exception):
    pass
class ForumBodyCannotBeEmpty(Exception):
    pass
class ForumSubjectCannotBeEmptyOnTopicPost(Exception):
    pass
class ForumCannotLocateParentPost(Exception):
    pass
class ForumThreadLockedForReplies(Exception):
    pass
class ForumUnknownSqlResultDuringCreatePost(Exception):
    pass
class ForumUnknownTagCreationError(Exception):
    pass
class ForumUnknownSqlResultDuringTagItem(Exception):
    pass
class ForumUnknownExceptionCreatePost(Exception):
    pass
class ForumQuestionMustBeTopicPost(Exception):
    pass
class ForumExceptionDuringTagSearch(Exception):
    pass
class ForumExceptionDuringTopicRetrieval(Exception):
    pass
class ForumAliasedTagError(Exception):
    pass
class ForumCannotLocateThread(Exception):
    pass
class ForumUnknownExceptionEditPost(Exception):
    pass
class ForumCannotLocatePost(Exception):
    pass
class ForumUnknownExceptionGetOrCreateTags(Exception):
    pass
class ForumEditPermissionDenied(Exception):
    pass
class ForumUnknownSqlResultDuringTagIdRetrieval(Exception):
    pass
class ForumCannotGetRating(Exception):
    pass
class ForumUnknownExceptionGetRating(Exception):
    pass
class ForumRatingsAccessError(Exception):
    pass
class ForumRelatedPostAccessError(Exception):
    pass
class ForumLatestReplyAccessError(Exception):
    pass
class ForumUserStatusAccessError(Exception):
    pass
class ForumAuthorAccessError(Exception):
    pass
class ForumGroupAccessError(Exception):
    pass
class ForumUrlExpectedButMissing(Exception):
    pass
class ForumRepliesCannotBeEmpty(Exception):
    pass
class ForumRepliesCannotBeInDifferentGroups(Exception):
    pass
class ForumSubTopicCannotBeCreatedAtThisThreadLevel(Exception):
    pass
class ForumCannotCreateContentTopic(Exception):
    pass
class ForumTopicDoesNotExist(Exception):
    pass
class ForumContentCommentsNotAllowed(Exception):
    pass
class ForumUnknownSqlResultDuringEditPost(Exception):
    pass
class ForumUnknownSqlResultDuringGetPost(Exception):
    pass
class ForumPostValidationBadUrl(Exception):
    pass
class ForumBodyTooLong(Exception):
    pass
class ForumSubjectTooLong(Exception):
    pass
class ForumAnnouncementNotAllowed(Exception):
    pass
class ForumCannotShareOwnPost(Exception):
    pass
class ForumEditNoOp(Exception):
    pass
class ForumUnknownDatabaseErrorDuringGetPost(Exception):
    pass
class ForumExceeedMaximumRowLimit(Exception):
    pass
class ForumCannotSharePrivatePost(Exception):
    pass
class ForumCannotCrossPostBetweenGroups(Exception):
    pass
class ForumIncompatibleCategories(Exception):
    pass
class ForumCannotUseTheseCategoriesOnNonTopicPost(Exception):
    pass
class ForumCanOnlyDeleteTopics(Exception):
    pass
class ForumDeleteSqlException(Exception):
    pass
class ForumDeleteSqlUnknownResult(Exception):
    pass
class ForumTooManyTags(Exception):
    pass
class ForumCanOnlyRateTopics(Exception):
    pass
class ForumBannedPostsCannotBeEdited(Exception):
    pass
class ForumThreadRootIsBanned(Exception):
    pass
class ForumCannotUseOfficialTagCategoryAsTag(Exception):
    pass
class ForumAnswerCannotBeMadeOnCreatePost(Exception):
    pass
class ForumAnswerCannotBeMadeOnEditPost(Exception):
    pass
class ForumAnswerPostIdIsNotADirectReplyOfQuestion(Exception):
    pass
class ForumAnswerTopicIdIsNotAQuestion(Exception):
    pass
class ForumUnknownExceptionDuringMarkAnswer(Exception):
    pass
class ForumUnknownSqlResultDuringMarkAnswer(Exception):
    pass
class ForumCannotRateYourOwnPosts(Exception):
    pass
class ForumPollsMustBeTheFirstPostInTopic(Exception):
    pass
class ForumInvalidPollInput(Exception):
    pass
class ForumGroupAdminEditNonMember(Exception):
    pass
class ForumCannotEditModeratorEditedPost(Exception):
    pass
class ForumRequiresDestinyMembership(Exception):
    pass
class ForumUnexpectedError(Exception):
    pass
class GroupMembershipApplicationAlreadyResolved(Exception):
    pass
class GroupMembershipAlreadyApplied(Exception):
    pass
class GroupMembershipInsufficientPrivileges(Exception):
    pass
class GroupIdNotReturnedFromCreation(Exception):
    pass
class GroupSearchInvalidParameters(Exception):
    pass
class GroupMembershipPendingApplicationNotFound(Exception):
    pass
class GroupInvalidId(Exception):
    pass
class GroupInvalidMembershipId(Exception):
    pass
class GroupInvalidMembershipType(Exception):
    pass
class GroupMissingTags(Exception):
    pass
class GroupMembershipNotFound(Exception):
    pass
class GroupInvalidRating(Exception):
    pass
class GroupUserFollowingAccessError(Exception):
    pass
class GroupUserMembershipAccessError(Exception):
    pass
class GroupCreatorAccessError(Exception):
    pass
class GroupAdminAccessError(Exception):
    pass
class GroupPrivatePostNotViewable(Exception):
    pass
class GroupMembershipNotLoggedIn(Exception):
    pass
class GroupNotDeleted(Exception):
    pass
class GroupUnknownErrorUndeletingGroup(Exception):
    pass
class GroupDeleted(Exception):
    pass
class GroupNotFound(Exception):
    pass
class GroupMemberBanned(Exception):
    pass
class GroupMembershipClosed(Exception):
    pass
class GroupPrivatePostOverrideError(Exception):
    pass
class GroupNameTaken(Exception):
    pass
class GroupDeletionGracePeriodExpired(Exception):
    pass
class GroupCannotCheckBanStatus(Exception):
    pass
class GroupMaximumMembershipCountReached(Exception):
    pass
class NoDestinyAccountForClanPlatform(Exception):
    pass
class AlreadyRequestingMembershipForClanPlatform(Exception):
    pass
class AlreadyClanMemberOnPlatform(Exception):
    pass
class GroupJoinedCannotSetClanName(Exception):
    pass
class GroupLeftCannotClearClanName(Exception):
    pass
class GroupRelationshipRequestPending(Exception):
    pass
class GroupRelationshipRequestBlocked(Exception):
    pass
class GroupRelationshipRequestNotFound(Exception):
    pass
class GroupRelationshipBlockNotFound(Exception):
    pass
class GroupRelationshipNotFound(Exception):
    pass
class GroupAlreadyAllied(Exception):
    pass
class GroupAlreadyMember(Exception):
    pass
class GroupRelationshipAlreadyExists(Exception):
    pass
class InvalidGroupTypesForRelationshipRequest(Exception):
    pass
class GroupAtMaximumAlliances(Exception):
    pass
class GroupCannotSetClanOnlySettings(Exception):
    pass
class ClanCannotSetTwoDefaultPostTypes(Exception):
    pass
class GroupMemberInvalidMemberType(Exception):
    pass
class GroupInvalidPlatformType(Exception):
    pass
class GroupMemberInvalidSort(Exception):
    pass
class GroupInvalidResolveState(Exception):
    pass
class ClanAlreadyEnabledForPlatform(Exception):
    pass
class ClanNotEnabledForPlatform(Exception):
    pass
class ClanEnabledButCouldNotJoinNoAccount(Exception):
    pass
class ClanEnabledButCouldNotJoinAlreadyMember(Exception):
    pass
class ClanCannotJoinNoCredential(Exception):
    pass
class NoClanMembershipForPlatform(Exception):
    pass
class GroupToGroupFollowLimitReached(Exception):
    pass
class ChildGroupAlreadyInAlliance(Exception):
    pass
class OwnerGroupAlreadyInAlliance(Exception):
    pass
class AllianceOwnerCannotJoinAlliance(Exception):
    pass
class GroupNotInAlliance(Exception):
    pass
class ChildGroupCannotInviteToAlliance(Exception):
    pass
class GroupToGroupAlreadyFollowed(Exception):
    pass
class GroupToGroupNotFollowing(Exception):
    pass
class ClanMaximumMembershipReached(Exception):
    pass
class ClanNameNotValid(Exception):
    pass
class ClanNameNotValidError(Exception):
    pass
class AllianceOwnerNotDefined(Exception):
    pass
class AllianceChildNotDefined(Exception):
    pass
class ClanNameIllegalCharacters(Exception):
    pass
class ClanTagIllegalCharacters(Exception):
    pass
class ClanRequiresInvitation(Exception):
    pass
class ActivitiesUnknownException(Exception):
    pass
class ActivitiesParameterNull(Exception):
    pass
class ActivityCountsDiabled(Exception):
    pass
class ActivitySearchInvalidParameters(Exception):
    pass
class ActivityPermissionDenied(Exception):
    pass
class ShareAlreadyShared(Exception):
    pass
class ActivityLoggingDisabled(Exception):
    pass
class ItemAlreadyFollowed(Exception):
    pass
class ItemNotFollowed(Exception):
    pass
class CannotFollowSelf(Exception):
    pass
class GroupFollowLimitExceeded(Exception):
    pass
class TagFollowLimitExceeded(Exception):
    pass
class UserFollowLimitExceeded(Exception):
    pass
class FollowUnsupportedEntityType(Exception):
    pass
class NoValidTagsInList(Exception):
    pass
class BelowMinimumSuggestionLength(Exception):
    pass
class CannotGetSuggestionsOnMultipleTagsSimultaneously(Exception):
    pass
class NotAValidPartialTag(Exception):
    pass
class TagSuggestionsUnknownSqlResult(Exception):
    pass
class TagsUnableToLoadPopularTagsFromDatabase(Exception):
    pass
class TagInvalid(Exception):
    pass
class TagNotFound(Exception):
    pass
class SingleTagExpected(Exception):
    pass
class IgnoreInvalidParameters(Exception):
    pass
class IgnoreSqlException(Exception):
    pass
class IgnoreErrorRetrievingGroupPermissions(Exception):
    pass
class IgnoreErrorInsufficientPermission(Exception):
    pass
class IgnoreErrorRetrievingItem(Exception):
    pass
class IgnoreCannotIgnoreSelf(Exception):
    pass
class IgnoreIllegalType(Exception):
    pass
class IgnoreNotFound(Exception):
    pass
class IgnoreUserGloballyIgnored(Exception):
    pass
class IgnoreUserIgnored(Exception):
    pass
class NotificationSettingInvalid(Exception):
    pass
class PSNExExpiredTicket(Exception):
    pass
class PSNExForbidden(Exception):
    pass
class PSNExSystemDisabled(Exception):
    pass
class PSNFriendsMissingTicket(Exception):
    pass
class PsnApiErrorCodeUnknown(Exception):
    pass
class PsnApiErrorWebException(Exception):
    pass
class PsnApiBadRequest(Exception):
    pass
class PsnApiAccessTokenRequired(Exception):
    pass
class PsnApiInvalidAccessToken(Exception):
    pass
class PsnApiExpiredAccessToken(Exception):
    pass
class PsnApiBannedUser(Exception):
    pass
class PsnApiAccountUpgradeRequired(Exception):
    pass
class PsnApiServiceTemporarilyUnavailable(Exception):
    pass
class PsnApiServerBusy(Exception):
    pass
class PsnApiUnderMaintenance(Exception):
    pass
class PsnApiProfileUserNotFound(Exception):
    pass
class PsnApiProfilePrivacyRestriction(Exception):
    pass
class PsnApiProfileUnderMaintenance(Exception):
    pass
class PsnApiAccountAttributeMissing(Exception):
    pass
class XblExSystemDisabled(Exception):
    pass
class XblExUnknownError(Exception):
    pass
class ReportNotYetResolved(Exception):
    pass
class ReportOverturnDoesNotChangeDecision(Exception):
    pass
class ReportNotFound(Exception):
    pass
class ReportAlreadyReported(Exception):
    pass
class ReportInvalidResolution(Exception):
    pass
class LegacyGameStatsSystemDisabled(Exception):
    pass
class LegacyGameStatsUnknownError(Exception):
    pass
class LegacyGameStatsMalformedSneakerNetCode(Exception):
    pass
class DestinyAccountAcquisitionFailure(Exception):
    pass
class DestinyAccountNotFound(Exception):
    pass
class DestinyBuildStatsDatabaseError(Exception):
    pass
class DestinyCharacterStatsDatabaseError(Exception):
    pass
class DestinyPvPStatsDatabaseError(Exception):
    pass
class DestinyPvEStatsDatabaseError(Exception):
    pass
class DestinyGrimoireStatsDatabaseError(Exception):
    pass
class DestinyStatsParameterMembershipTypeParseError(Exception):
    pass
class DestinyStatsParameterMembershipIdParseError(Exception):
    pass
class DestinyStatsParameterRangeParseError(Exception):
    pass
class DestinyStringItemHashNotFound(Exception):
    pass
class DestinyStringSetNotFound(Exception):
    pass
class DestinyContentLookupNotFoundForKey(Exception):
    pass
class DestinyContentItemNotFound(Exception):
    pass
class DestinyContentSectionNotFound(Exception):
    pass
class DestinyContentPropertyNotFound(Exception):
    pass
class DestinyContentConfigNotFound(Exception):
    pass
class DestinyContentPropertyBucketValueNotFound(Exception):
    pass
class DestinyUnexpectedError(Exception):
    pass
class DestinyInvalidAction(Exception):
    pass
class DestinyCharacterNotFound(Exception):
    pass
class DestinyInvalidFlag(Exception):
    pass
class DestinyInvalidRequest(Exception):
    pass
class DestinyItemNotFound(Exception):
    pass
class DestinyInvalidCustomizationChoices(Exception):
    pass
class DestinyVendorItemNotFound(Exception):
    pass
class DestinyInternalError(Exception):
    pass
class DestinyVendorNotFound(Exception):
    pass
class DestinyRecentActivitiesDatabaseError(Exception):
    pass
class DestinyItemBucketNotFound(Exception):
    pass
class DestinyInvalidMembershipType(Exception):
    pass
class DestinyVersionIncompatibility(Exception):
    pass
class DestinyItemAlreadyInInventory(Exception):
    pass
class DestinyBucketNotFound(Exception):
    pass
class DestinyCharacterNotInTower(Exception):
    pass
class DestinyCharacterNotLoggedIn(Exception):
    pass
class DestinyDefinitionsNotLoaded(Exception):
    pass
class DestinyInventoryFull(Exception):
    pass
class DestinyItemFailedLevelCheck(Exception):
    pass
class DestinyItemFailedUnlockCheck(Exception):
    pass
class DestinyItemUnequippable(Exception):
    pass
class DestinyItemUniqueEquipRestricted(Exception):
    pass
class DestinyNoRoomInDestination(Exception):
    pass
class DestinyServiceFailure(Exception):
    pass
class DestinyServiceRetired(Exception):
    pass
class DestinyTransferFailed(Exception):
    pass
class DestinyTransferNotFoundForSourceBucket(Exception):
    pass
class DestinyUnexpectedResultInVendorTransferCheck(Exception):
    pass
class DestinyUniquenessViolation(Exception):
    pass
class DestinyErrorDeserializationFailure(Exception):
    pass
class DestinyValidAccountTicketRequired(Exception):
    pass
class DestinyShardRelayClientTimeout(Exception):
    pass
class DestinyShardRelayProxyTimeout(Exception):
    pass
class FbInvalidRequest(Exception):
    pass
class FbRedirectMismatch(Exception):
    pass
class FbAccessDenied(Exception):
    pass
class FbUnsupportedResponseType(Exception):
    pass
class FbInvalidScope(Exception):
    pass
class FbUnsupportedGrantType(Exception):
    pass
class FbInvalidGrant(Exception):
    pass
class InvitationExpired(Exception):
    pass
class InvitationUnknownType(Exception):
    pass
class InvitationInvalidResponseStatus(Exception):
    pass
class InvitationInvalidType(Exception):
    pass
class InvitationAlreadyPending(Exception):
    pass
class InvitationInsufficientPermission(Exception):
    pass
class InvitationInvalidCode(Exception):
    pass
class InvitationInvalidTargetState(Exception):
    pass
class InvitationCannotBeReactivated(Exception):
    pass
class InvitationAutoApproved(Exception):
    pass
class InvitationNoRecipients(Exception):
    pass
class InvitationGroupCannotSendToSelf(Exception):
    pass
class InvitationTooManyRecipients(Exception):
    pass
class InvitationInvalid(Exception):
    pass
class InvitationNotFound(Exception):
    pass
class TokenInvalid(Exception):
    pass
class TokenBadFormat(Exception):
    pass
class TokenAlreadyClaimed(Exception):
    pass
class TokenAlreadyClaimedSelf(Exception):
    pass
class TokenThrottling(Exception):
    pass
class TokenUnknownRedemptionFailure(Exception):
    pass
class TokenPurchaseClaimFailedAfterTokenClaimed(Exception):
    pass
class TokenUserAlreadyOwnsOffer(Exception):
    pass
class TokenInvalidOfferKey(Exception):
    pass
class TokenEmailNotValidated(Exception):
    pass
class TokenProvisioningBadVendorOrOffer(Exception):
    pass
class TokenPurchaseHistoryUnknownError(Exception):
    pass
class TokenThrottleStateUnknownError(Exception):
    pass
class TokenUserAgeNotVerified(Exception):
    pass
class TokenExceededOfferMaximum(Exception):
    pass
class TokenNoAvailableUnlocks(Exception):
    pass
class TokenMarketplaceInvalidPlatform(Exception):
    pass
class TokenNoMarketplaceCodesFound(Exception):
    pass
class TokenOfferNotAvailableForRedemption(Exception):
    pass
class TokenUnlockPartialFailure(Exception):
    pass
class TokenMarketplaceInvalidRegion(Exception):
    pass
class TokenOfferExpired(Exception):
    pass

e_map = {
    2 : TransportException,
    3 : UnhandledException,
    4 : NotImplemented,
    5 : SystemDisabled,
    6 : FailedToLoadAvailableLocalesConfiguration,
    7 : ParameterParseFailure,
    8 : ParameterInvalidRange,
    9 : BadRequest,
    10 : AuthenticationInvalid,
    11 : DataNotFound,
    12 : InsufficientPrivileges,
    13 : Duplicate,
    14 : UnknownSqlResult,
    15 : ValidationError,
    16 : ValidationMissingFieldError,
    17 : ValidationInvalidInputError,
    18 : InvalidParameters,
    19 : ParameterNotFound,
    20 : UnhandledHttpException,
    21 : NotFound,
    22 : WebAuthModuleAsyncFailed,
    23 : InvalidReturnValue,
    24 : UserBanned,
    25 : InvalidPostBody,
    26 : MissingPostBody,
    27 : ExternalServiceTimeout,
    28 : ValidationLengthError,
    29 : ValidationRangeError,
    30 : JsonDeserializationError,
    31 : ThrottleLimitExceeded,
    32 : ValidationTagError,
    33 : ValidationProfanityError,
    34 : ValidationUrlFormatError,
    35 : ThrottleLimitExceededMinutes,
    36 : ThrottleLimitExceededMomentarily,
    37 : ThrottleLimitExceededSeconds,
    38 : ExternalServiceUnknown,
    39 : ValidationWordLengthError,
    40 : ValidationInvisibleUnicode,
    41 : ValidationBadNames,
    42 : ExternalServiceFailed,
    43 : ServiceRetired,
    44 : UnknownSqlException,
    45 : UnsupportedLocale,
    46 : InvalidPageNumber,
    47 : MaximumPageSizeExceeded,
    48 : ServiceUnsupported,
    49 : ValidationMaximumUnicodeCombiningCharacters,
    90 : UnableToUnPairMobileApp,
    91 : UnableToPairMobileApp,
    92 : CannotUseMobileAuthWithNonMobileProvider,
    93 : MissingDeviceCookie,
    94 : FacebookTokenExpired,
    95 : AuthTicketRequired,
    96 : CookieContextRequired,
    97 : UnknownAuthenticationError,
    98 : BungieNetAccountCreationRequired,
    99 : WebAuthRequired,
    100 : ContentUnknownSqlResult,
    101 : ContentNeedUniquePath,
    102 : ContentSqlException,
    103 : ContentNotFound,
    104 : ContentSuccessWithTagAddFail,
    105 : ContentSearchMissingParameters,
    106 : ContentInvalidId,
    107 : ContentPhysicalFileDeletionError,
    108 : ContentPhysicalFileCreationError,
    109 : ContentPerforceSubmissionError,
    110 : ContentPerforceInitializationError,
    111 : ContentDeploymentPackageNotReadyError,
    112 : ContentUploadFailed,
    113 : ContentTooManyResults,
    115 : ContentInvalidState,
    116 : ContentNavigationParentNotFound,
    117 : ContentNavigationParentUpdateError,
    118 : DeploymentPackageNotEditable,
    119 : ContentValidationError,
    120 : ContentPropertiesValidationError,
    121 : ContentTypeNotFound,
    122 : DeploymentPackageNotFound,
    123 : ContentSearchInvalidParameters,
    124 : ContentItemPropertyAggregationError,
    125 : DeploymentPackageFileNotFound,
    126 : ContentPerforceFileHistoryNotFound,
    127 : ContentAssetZipCreationFailure,
    128 : ContentAssetZipCreationBusy,
    129 : ContentProjectNotFound,
    130 : ContentFolderNotFound,
    131 : ContentPackagesInconsistent,
    132 : ContentPackagesInvalidState,
    133 : ContentPackagesInconsistentType,
    134 : ContentCannotDeletePackage,
    135 : ContentLockedForChanges,
    136 : ContentFileUploadFailed,
    137 : ContentNotReviewed,
    138 : ContentPermissionDenied,
    139 : ContentInvalidExternalUrl,
    140 : ContentExternalFileCannotBeImportedLocally,
    141 : ContentTagSaveFailure,
    142 : ContentPerforceUnmatchedFileError,
    143 : ContentPerforceChangelistResultNotFound,
    144 : ContentPerforceChangelistFileItemsNotFound,
    145 : ContentPerforceInvalidRevisionError,
    146 : ContentUnloadedSaveResult,
    147 : ContentPropertyInvalidNumber,
    148 : ContentPropertyInvalidUrl,
    149 : ContentPropertyInvalidDate,
    150 : ContentPropertyInvalidSet,
    151 : ContentPropertyCannotDeserialize,
    152 : ContentRegexValidationFailOnProperty,
    153 : ContentMaxLengthFailOnProperty,
    154 : ContentPropertyUnexpectedDeserializationError,
    155 : ContentPropertyRequired,
    156 : ContentCannotCreateFile,
    157 : ContentInvalidMigrationFile,
    158 : ContentMigrationAlteringProcessedItem,
    159 : ContentPropertyDefinitionNotFound,
    160 : ContentReviewDataChanged,
    161 : ContentRollbackRevisionNotInPackage,
    162 : ContentItemNotBasedOnLatestRevision,
    163 : ContentUnauthorized,
    164 : ContentCannotCreateDeploymentPackage,
    165 : ContentUserNotFound,
    166 : ContentLocalePermissionDenied,
    167 : ContentInvalidLinkToInternalEnvironment,
    168 : ContentInvalidBlacklistedContent,
    200 : UserNonUniqueName,
    201 : UserManualLinkingStepRequired,
    202 : UserCreateUnknownSqlResult,
    203 : UserCreateUnknownSqlException,
    204 : UserMalformedMembershipId,
    205 : UserCannotFindRequestedUser,
    206 : UserCannotLoadAccountCredentialLinkInfo,
    207 : UserInvalidMobileAppType,
    208 : UserMissingMobilePairingInfo,
    209 : UserCannotGenerateMobileKeyWhileUsingMobileCredential,
    210 : UserGenerateMobileKeyExistingSlotCollision,
    211 : UserDisplayNameMissingOrInvalid,
    212 : UserCannotLoadAccountProfileData,
    213 : UserCannotSaveUserProfileData,
    214 : UserEmailMissingOrInvalid,
    215 : UserTermsOfUseRequired,
    216 : UserCannotCreateNewAccountWhileLoggedIn,
    217 : UserCannotResolveCentralAccount,
    218 : UserInvalidAvatar,
    219 : UserMissingCreatedUserResult,
    220 : UserCannotChangeUniqueNameYet,
    221 : UserCannotChangeDisplayNameYet,
    222 : UserCannotChangeEmail,
    223 : UserUniqueNameMustStartWithLetter,
    224 : UserNoLinkedAccountsSupportFriendListings,
    225 : UserAcknowledgmentTableFull,
    300 : MessagingUnknownError,
    301 : MessagingSelfError,
    302 : MessagingSendThrottle,
    303 : MessagingNoBody,
    304 : MessagingTooManyUsers,
    305 : MessagingCanNotLeaveConversation,
    306 : MessagingUnableToSend,
    307 : MessagingDeletedUserForbidden,
    308 : MessagingCannotDeleteExternalConversation,
    309 : MessagingGroupChatDisabled,
    310 : MessagingMustIncludeSelfInPrivateMessage,
    400 : AddSurveyAnswersUnknownSqlException,
    500 : ForumBodyCannotBeEmpty,
    501 : ForumSubjectCannotBeEmptyOnTopicPost,
    502 : ForumCannotLocateParentPost,
    503 : ForumThreadLockedForReplies,
    504 : ForumUnknownSqlResultDuringCreatePost,
    505 : ForumUnknownTagCreationError,
    506 : ForumUnknownSqlResultDuringTagItem,
    507 : ForumUnknownExceptionCreatePost,
    508 : ForumQuestionMustBeTopicPost,
    509 : ForumExceptionDuringTagSearch,
    510 : ForumExceptionDuringTopicRetrieval,
    511 : ForumAliasedTagError,
    512 : ForumCannotLocateThread,
    513 : ForumUnknownExceptionEditPost,
    514 : ForumCannotLocatePost,
    515 : ForumUnknownExceptionGetOrCreateTags,
    516 : ForumEditPermissionDenied,
    517 : ForumUnknownSqlResultDuringTagIdRetrieval,
    518 : ForumCannotGetRating,
    519 : ForumUnknownExceptionGetRating,
    520 : ForumRatingsAccessError,
    521 : ForumRelatedPostAccessError,
    522 : ForumLatestReplyAccessError,
    523 : ForumUserStatusAccessError,
    524 : ForumAuthorAccessError,
    525 : ForumGroupAccessError,
    526 : ForumUrlExpectedButMissing,
    527 : ForumRepliesCannotBeEmpty,
    528 : ForumRepliesCannotBeInDifferentGroups,
    529 : ForumSubTopicCannotBeCreatedAtThisThreadLevel,
    530 : ForumCannotCreateContentTopic,
    531 : ForumTopicDoesNotExist,
    532 : ForumContentCommentsNotAllowed,
    533 : ForumUnknownSqlResultDuringEditPost,
    534 : ForumUnknownSqlResultDuringGetPost,
    535 : ForumPostValidationBadUrl,
    536 : ForumBodyTooLong,
    537 : ForumSubjectTooLong,
    538 : ForumAnnouncementNotAllowed,
    539 : ForumCannotShareOwnPost,
    540 : ForumEditNoOp,
    541 : ForumUnknownDatabaseErrorDuringGetPost,
    542 : ForumExceeedMaximumRowLimit,
    543 : ForumCannotSharePrivatePost,
    544 : ForumCannotCrossPostBetweenGroups,
    555 : ForumIncompatibleCategories,
    556 : ForumCannotUseTheseCategoriesOnNonTopicPost,
    557 : ForumCanOnlyDeleteTopics,
    558 : ForumDeleteSqlException,
    559 : ForumDeleteSqlUnknownResult,
    560 : ForumTooManyTags,
    561 : ForumCanOnlyRateTopics,
    562 : ForumBannedPostsCannotBeEdited,
    563 : ForumThreadRootIsBanned,
    564 : ForumCannotUseOfficialTagCategoryAsTag,
    565 : ForumAnswerCannotBeMadeOnCreatePost,
    566 : ForumAnswerCannotBeMadeOnEditPost,
    567 : ForumAnswerPostIdIsNotADirectReplyOfQuestion,
    568 : ForumAnswerTopicIdIsNotAQuestion,
    569 : ForumUnknownExceptionDuringMarkAnswer,
    570 : ForumUnknownSqlResultDuringMarkAnswer,
    571 : ForumCannotRateYourOwnPosts,
    572 : ForumPollsMustBeTheFirstPostInTopic,
    573 : ForumInvalidPollInput,
    574 : ForumGroupAdminEditNonMember,
    575 : ForumCannotEditModeratorEditedPost,
    576 : ForumRequiresDestinyMembership,
    577 : ForumUnexpectedError,
    601 : GroupMembershipApplicationAlreadyResolved,
    602 : GroupMembershipAlreadyApplied,
    603 : GroupMembershipInsufficientPrivileges,
    604 : GroupIdNotReturnedFromCreation,
    605 : GroupSearchInvalidParameters,
    606 : GroupMembershipPendingApplicationNotFound,
    607 : GroupInvalidId,
    608 : GroupInvalidMembershipId,
    609 : GroupInvalidMembershipType,
    610 : GroupMissingTags,
    611 : GroupMembershipNotFound,
    612 : GroupInvalidRating,
    613 : GroupUserFollowingAccessError,
    614 : GroupUserMembershipAccessError,
    615 : GroupCreatorAccessError,
    616 : GroupAdminAccessError,
    617 : GroupPrivatePostNotViewable,
    618 : GroupMembershipNotLoggedIn,
    619 : GroupNotDeleted,
    620 : GroupUnknownErrorUndeletingGroup,
    621 : GroupDeleted,
    622 : GroupNotFound,
    623 : GroupMemberBanned,
    624 : GroupMembershipClosed,
    625 : GroupPrivatePostOverrideError,
    626 : GroupNameTaken,
    627 : GroupDeletionGracePeriodExpired,
    628 : GroupCannotCheckBanStatus,
    629 : GroupMaximumMembershipCountReached,
    630 : NoDestinyAccountForClanPlatform,
    631 : AlreadyRequestingMembershipForClanPlatform,
    632 : AlreadyClanMemberOnPlatform,
    633 : GroupJoinedCannotSetClanName,
    634 : GroupLeftCannotClearClanName,
    635 : GroupRelationshipRequestPending,
    636 : GroupRelationshipRequestBlocked,
    637 : GroupRelationshipRequestNotFound,
    638 : GroupRelationshipBlockNotFound,
    639 : GroupRelationshipNotFound,
    641 : GroupAlreadyAllied,
    642 : GroupAlreadyMember,
    643 : GroupRelationshipAlreadyExists,
    644 : InvalidGroupTypesForRelationshipRequest,
    646 : GroupAtMaximumAlliances,
    647 : GroupCannotSetClanOnlySettings,
    648 : ClanCannotSetTwoDefaultPostTypes,
    649 : GroupMemberInvalidMemberType,
    650 : GroupInvalidPlatformType,
    651 : GroupMemberInvalidSort,
    652 : GroupInvalidResolveState,
    653 : ClanAlreadyEnabledForPlatform,
    654 : ClanNotEnabledForPlatform,
    655 : ClanEnabledButCouldNotJoinNoAccount,
    656 : ClanEnabledButCouldNotJoinAlreadyMember,
    657 : ClanCannotJoinNoCredential,
    658 : NoClanMembershipForPlatform,
    659 : GroupToGroupFollowLimitReached,
    660 : ChildGroupAlreadyInAlliance,
    661 : OwnerGroupAlreadyInAlliance,
    662 : AllianceOwnerCannotJoinAlliance,
    663 : GroupNotInAlliance,
    664 : ChildGroupCannotInviteToAlliance,
    665 : GroupToGroupAlreadyFollowed,
    666 : GroupToGroupNotFollowing,
    667 : ClanMaximumMembershipReached,
    668 : ClanNameNotValid,
    669 : ClanNameNotValidError,
    670 : AllianceOwnerNotDefined,
    671 : AllianceChildNotDefined,
    672 : ClanNameIllegalCharacters,
    673 : ClanTagIllegalCharacters,
    674 : ClanRequiresInvitation,
    701 : ActivitiesUnknownException,
    702 : ActivitiesParameterNull,
    703 : ActivityCountsDiabled,
    704 : ActivitySearchInvalidParameters,
    705 : ActivityPermissionDenied,
    706 : ShareAlreadyShared,
    707 : ActivityLoggingDisabled,
    801 : ItemAlreadyFollowed,
    802 : ItemNotFollowed,
    803 : CannotFollowSelf,
    804 : GroupFollowLimitExceeded,
    805 : TagFollowLimitExceeded,
    806 : UserFollowLimitExceeded,
    807 : FollowUnsupportedEntityType,
    900 : NoValidTagsInList,
    901 : BelowMinimumSuggestionLength,
    902 : CannotGetSuggestionsOnMultipleTagsSimultaneously,
    903 : NotAValidPartialTag,
    904 : TagSuggestionsUnknownSqlResult,
    905 : TagsUnableToLoadPopularTagsFromDatabase,
    906 : TagInvalid,
    907 : TagNotFound,
    908 : SingleTagExpected,
    1000 : IgnoreInvalidParameters,
    1001 : IgnoreSqlException,
    1002 : IgnoreErrorRetrievingGroupPermissions,
    1003 : IgnoreErrorInsufficientPermission,
    1004 : IgnoreErrorRetrievingItem,
    1005 : IgnoreCannotIgnoreSelf,
    1006 : IgnoreIllegalType,
    1007 : IgnoreNotFound,
    1008 : IgnoreUserGloballyIgnored,
    1009 : IgnoreUserIgnored,
    1100 : NotificationSettingInvalid,
    1204 : PSNExExpiredTicket,
    1205 : PSNExForbidden,
    1218 : PSNExSystemDisabled,
    1219 : PSNFriendsMissingTicket,
    1223 : PsnApiErrorCodeUnknown,
    1224 : PsnApiErrorWebException,
    1225 : PsnApiBadRequest,
    1226 : PsnApiAccessTokenRequired,
    1227 : PsnApiInvalidAccessToken,
    1228 : PsnApiExpiredAccessToken,
    1229 : PsnApiBannedUser,
    1230 : PsnApiAccountUpgradeRequired,
    1231 : PsnApiServiceTemporarilyUnavailable,
    1232 : PsnApiServerBusy,
    1233 : PsnApiUnderMaintenance,
    1234 : PsnApiProfileUserNotFound,
    1235 : PsnApiProfilePrivacyRestriction,
    1236 : PsnApiProfileUnderMaintenance,
    1237 : PsnApiAccountAttributeMissing,
    1300 : XblExSystemDisabled,
    1301 : XblExUnknownError,
    1400 : ReportNotYetResolved,
    1401 : ReportOverturnDoesNotChangeDecision,
    1402 : ReportNotFound,
    1403 : ReportAlreadyReported,
    1404 : ReportInvalidResolution,
    1500 : LegacyGameStatsSystemDisabled,
    1501 : LegacyGameStatsUnknownError,
    1502 : LegacyGameStatsMalformedSneakerNetCode,
    1600 : DestinyAccountAcquisitionFailure,
    1601 : DestinyAccountNotFound,
    1602 : DestinyBuildStatsDatabaseError,
    1603 : DestinyCharacterStatsDatabaseError,
    1604 : DestinyPvPStatsDatabaseError,
    1605 : DestinyPvEStatsDatabaseError,
    1606 : DestinyGrimoireStatsDatabaseError,
    1607 : DestinyStatsParameterMembershipTypeParseError,
    1608 : DestinyStatsParameterMembershipIdParseError,
    1609 : DestinyStatsParameterRangeParseError,
    1610 : DestinyStringItemHashNotFound,
    1611 : DestinyStringSetNotFound,
    1612 : DestinyContentLookupNotFoundForKey,
    1613 : DestinyContentItemNotFound,
    1614 : DestinyContentSectionNotFound,
    1615 : DestinyContentPropertyNotFound,
    1616 : DestinyContentConfigNotFound,
    1617 : DestinyContentPropertyBucketValueNotFound,
    1618 : DestinyUnexpectedError,
    1619 : DestinyInvalidAction,
    1620 : DestinyCharacterNotFound,
    1621 : DestinyInvalidFlag,
    1622 : DestinyInvalidRequest,
    1623 : DestinyItemNotFound,
    1624 : DestinyInvalidCustomizationChoices,
    1625 : DestinyVendorItemNotFound,
    1626 : DestinyInternalError,
    1627 : DestinyVendorNotFound,
    1628 : DestinyRecentActivitiesDatabaseError,
    1629 : DestinyItemBucketNotFound,
    1630 : DestinyInvalidMembershipType,
    1631 : DestinyVersionIncompatibility,
    1632 : DestinyItemAlreadyInInventory,
    1633 : DestinyBucketNotFound,
    1634 : DestinyCharacterNotInTower,
    1635 : DestinyCharacterNotLoggedIn,
    1636 : DestinyDefinitionsNotLoaded,
    1637 : DestinyInventoryFull,
    1638 : DestinyItemFailedLevelCheck,
    1639 : DestinyItemFailedUnlockCheck,
    1640 : DestinyItemUnequippable,
    1641 : DestinyItemUniqueEquipRestricted,
    1642 : DestinyNoRoomInDestination,
    1643 : DestinyServiceFailure,
    1644 : DestinyServiceRetired,
    1645 : DestinyTransferFailed,
    1646 : DestinyTransferNotFoundForSourceBucket,
    1647 : DestinyUnexpectedResultInVendorTransferCheck,
    1648 : DestinyUniquenessViolation,
    1649 : DestinyErrorDeserializationFailure,
    1650 : DestinyValidAccountTicketRequired,
    1651 : DestinyShardRelayClientTimeout,
    1652 : DestinyShardRelayProxyTimeout,
    1800 : FbInvalidRequest,
    1801 : FbRedirectMismatch,
    1802 : FbAccessDenied,
    1803 : FbUnsupportedResponseType,
    1804 : FbInvalidScope,
    1805 : FbUnsupportedGrantType,
    1806 : FbInvalidGrant,
    1900 : InvitationExpired,
    1901 : InvitationUnknownType,
    1902 : InvitationInvalidResponseStatus,
    1903 : InvitationInvalidType,
    1904 : InvitationAlreadyPending,
    1905 : InvitationInsufficientPermission,
    1906 : InvitationInvalidCode,
    1907 : InvitationInvalidTargetState,
    1908 : InvitationCannotBeReactivated,
    1909 : InvitationAutoApproved,
    1910 : InvitationNoRecipients,
    1911 : InvitationGroupCannotSendToSelf,
    1912 : InvitationTooManyRecipients,
    1913 : InvitationInvalid,
    1914 : InvitationNotFound,
    2000 : TokenInvalid,
    2001 : TokenBadFormat,
    2002 : TokenAlreadyClaimed,
    2003 : TokenAlreadyClaimedSelf,
    2004 : TokenThrottling,
    2005 : TokenUnknownRedemptionFailure,
    2006 : TokenPurchaseClaimFailedAfterTokenClaimed,
    2007 : TokenUserAlreadyOwnsOffer,
    2008 : TokenInvalidOfferKey,
    2009 : TokenEmailNotValidated,
    2010 : TokenProvisioningBadVendorOrOffer,
    2011 : TokenPurchaseHistoryUnknownError,
    2012 : TokenThrottleStateUnknownError,
    2013 : TokenUserAgeNotVerified,
    2014 : TokenExceededOfferMaximum,
    2015 : TokenNoAvailableUnlocks,
    2016 : TokenMarketplaceInvalidPlatform,
    2017 : TokenNoMarketplaceCodesFound,
    2018 : TokenOfferNotAvailableForRedemption,
    2019 : TokenUnlockPartialFailure,
    2020 : TokenMarketplaceInvalidRegion,
    2021 : TokenOfferExpired
}

def raise_destiny_exception(code):
    raise e_map[code]
