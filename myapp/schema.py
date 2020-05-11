from graphene_django import DjangoObjectType
import graphene
from myapp.models import VinylModel


class VinylType(DjangoObjectType):
    class Meta:
        model = VinylModel


class Query(graphene.ObjectType):
    vinyls = graphene.List(VinylType)

    def resolve_vinyls(self, info):
        return VinylModel.objects.all()


class CreateVinyl(graphene.Mutation):
    id = graphene.Int()
    song_name = graphene.String()
    artist = graphene.String()
    album_name = graphene.String()

    class Arguments:
        song_name = graphene.String()
        artist = graphene.String()
        album_name = graphene.String()

    def mutate(self, info, song_name, album_name,artist):
        vinyl = VinylModel(song_name=song_name, album_name=album_name,artist=artist)
        vinyl.save()

        return CreateVinyl(
            id=vinyl.id,
            song_name=vinyl.song_name,
            album_name=vinyl.album_name,
            artist=vinyl.artist,
        )


class Mutation(graphene.ObjectType):
    create_vinyl = CreateVinyl.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation)